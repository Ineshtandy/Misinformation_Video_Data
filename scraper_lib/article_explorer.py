def explore(content_list):
    from bs4 import BeautifulSoup
    from scraper_lib.rep_text import representative_text
    from scraper_lib.link_extracter import extract_domain

    json_results = []

    for article_content in content_list:

        # initialize soup for cur_article
        soup = BeautifulSoup(article_content, 'html.parser')

        # HEADLINE
        soup_heading = soup.find('section', class_='title-container').find('h1') if soup.find('section', class_='title-container') is not None else None
        cur_heading = soup_heading.text if soup_heading is not None else "None"
        print('heading done')

        # VERACITY
        soup_rating = soup.find('div', class_='rating_title_wrap')
        rating_info = soup_rating.text if soup_rating is not None else "None"
        stripped_rating = ""
        for ch in rating_info:
            if ch.isalpha():
                stripped_rating += ch
        cur_veracity_rating = stripped_rating[:len(stripped_rating) - 15]
        print(cur_veracity_rating, ' - veracity done')

        # video links
        soup_links = soup.find('article', id='article-content').find_all('a', target='_blank') if soup.find('article', id='article-content') is not None else []
        video_links = [link for link in soup_links if link is not None]
        print('video link extraction done')

        for idx, video_link in enumerate(video_links):

            if idx == 0:
                # REPRESENTATIVE TEXT
                cur_rep_text = representative_text(video_link['href'])

                # original source name
                cur_domain_name = extract_domain(video_link['href'])

                # original source link
                cur_orig_src = video_link['href']

            # call video searcher here
                # check 1: check for m3u8 files in network requests on page load, works for embedded
                # check 2: for video in soup.find_all('video')
                    # if video.find('source'):
                        # if video.find('source')['type'] == "video/mp4":
                            # print(video.find('source')['src'])

            # call video downloader here

            print('first video extraction done')

        cur_details = {'headline': cur_heading,
                       'veracity': cur_veracity_rating,
                       'original_source': cur_domain_name,
                       'original_source_link': cur_orig_src,
                       'representative_text': cur_rep_text
                       }
        
        json_results.append(cur_details)

    return json_results

        




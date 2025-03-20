# Headline: The title of the Snopes article (e.g., Fake Video Shows Trump Announcing Executive Order to Allow Slurs).
# Representative Text: A short excerpt from the post (e.g., It’s happening).
# Original Source: The platform where the video was first shared (e.g., Twitter).
# Veracity: The Snopes fact-check result (e.g., False).
# Shareable Video Link: The direct link to the post containing the video (e.g., a Twitter post).
# Downloadable Video Link: A saved copy of the video (hosted on a shared drive).
# Additional Information: Any other relevant metadata that could enhance the dataset.

def article_soup(search_results):
    from bs4 import BeautifulSoup
    import json

    articles = set()

    for i, result in enumerate(search_results):
        soup = BeautifulSoup(result, 'html.parser')


        for article_info in soup.find_all('a', {'class' : 'gs-title'}):
            articles.add(article_info.get('href')) # treat bs4.element.tag as a dictionary


    return list(articles)

def extract_domain(url):
    import re
    # Regular expression to extract domain name
    pattern = r'^(?:https?://)?(?:www\.)?([^/]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


    






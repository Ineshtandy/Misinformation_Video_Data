# Headline: The title of the Snopes article (e.g., Fake Video Shows Trump Announcing Executive Order to Allow Slurs).
# Representative Text: A short excerpt from the post (e.g., It’s happening).
# Original Source: The platform where the video was first shared (e.g., Twitter).
# Veracity: The Snopes fact-check result (e.g., False).
# Shareable Video Link: The direct link to the post containing the video (e.g., a Twitter post).
# Downloadable Video Link: A saved copy of the video (hosted on a shared drive).
# Additional Information: Any other relevant metadata that could enhance the dataset.


from bs4 import BeautifulSoup
import json

articles = set()
for i in range(1,5,1):
    with open(f"page_source{i}.html") as data_file:
        soup = BeautifulSoup(data_file, 'html.parser')


    for article_info in soup.find_all('a', {'class' : 'gs-title'}):
        # cur_article_json = {"title": article_info.text, "link": article_info.get('href')} # treat bs4.element.tag as a dictionary
        # articles.append(cur_article_json)

        articles.add(article_info.get('href'))

    uniq_articles = set()

    # creating a set of only unique articles
    # for article in articles:
    #     article_dic = json.loads(article)
    #     uniq_articles.add(tuple(article_dic.items()))

    for article in articles:
        # output = json.dumps(article, indent = 1)
        # print(output)
        print(article)
    # print(articles[1].attrs.keys())

print(len(articles))


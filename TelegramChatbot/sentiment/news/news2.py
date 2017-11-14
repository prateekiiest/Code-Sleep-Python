import requests
import json
def getNews(source):
     url = 'https://newsapi.org/v1/articles?source=' + source + '&apiKey=4ab6ea3b79144fb6a3d36f8aa85f1eac'
     n = getContent(url)
     # print n['articles'][0]['url']

     news = []
     for item in n['articles']:
             news.append((item['title'], item['url']))
     return news

def getContent(url):
    con = requests.get(url)
    return json.loads(con.content.decode("utf8"))


print getNews('the-next-web')

import json
from news_scrapper import scrape as news_scrape
import requests
import time
import urllib
from vaderSentiment import vaderSentiment
from unidecode import unidecode
from Portfolio import portfolio

TOKEN = "" # token
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def getContent(url):
    con = requests.get(url)
    return json.loads(con.content.decode("utf8"))

####################################
def getNews(source):
    url = 'https://newsapi.org/v1/articles?source=' + source + '&apiKey=4ab6ea3b79144fb6a3d36f8aa85f1eac'
    n = getContent(url)
    # print n['articles'][0]['url']

    news = []
    for item in n['articles']:
        news.append((item['title'], item['url']))
    return news

def getSources(category):
    url = "https://newsapi.org/v1/sources?language=en&category=" + category
    s = getContent(url)
    sources = []
    for item in s['sources']:
        sources.append((item['name'], item['url'], item['id']))
    return sources
###################################

def getUpdates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
#    print url
    js = getContent(url)
    return js

def getLatestUpdate_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    #text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def computation(text):
    arr = text.split()

    if arr[0] == '/news':
        # do this
        print "the source is " + arr[1]
        news = getNews(arr[1])
        result = ''
        for n in news:
            result = result + unidecode(n[0]) + '\n' + unidecode(n[1]) + '\n\n'
        print result
    elif arr[0] == '/sources':
        print "the required category is " + arr[1]
        sources = getSources(arr[1])
        result = ''
        for s in sources:
            result = result + unidecode(s[0]) + '\n' + unidecode(s[1]) + '\n' + unidecode(s[2]) + '\n\n'

        print result
    elif arr[0] == '/portfolio':
        if arr[1] == 'show':
            result = portfolio.showPortfolio()	
        elif arr[1] == 'profit':
            result = "Current Profit is " + str(portfolio.calculate_profit())
	elif arr[1] == 'remove':
            ticker = arr[2]
	elif arr[1] == 'add':
            ticker = arr[2]
            price = arr[3]
            quantity = arr[4]
            ret = portfolio.insert_stock(ticker, quantity, price)
            if ret == True:
	       result = "Added Successfully\n."
	    else:
	       result = "Try Again, error encountered\n"
    return result

def main():
    last_update_id = None
    while True:
        updates = getUpdates(last_update_id)
        if len(updates["result"]) > 0:
            (text, chatid) = get_last_chat_id_and_text(updates)
            # perform computation on text.
            # print text
            result = computation(text)
            send_message(result, chatid)
            last_update_id = getLatestUpdate_id(updates) + 1
        time.sleep(0.5)


if __name__ == '__main__':
    main()

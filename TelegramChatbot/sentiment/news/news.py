import requests

def get_news(news_source, key = 'c8beb9bc3f544e52b2a449364c7156b4'):
	news_obj = requests.get('https://newsapi.org/v1/articles?source=' + news_source + '&sortBy=latest&apiKey='+key)
	news = []
	item_list =  news_obj.json()['articles']
	print item_list[0]['description']
	i = 0
	while i < len(item_list):
		news.append(item_list[i]['description'])
		i += 1
	return news

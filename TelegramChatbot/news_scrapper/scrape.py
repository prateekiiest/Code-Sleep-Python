from v import SentimentIntensityAnalyzer as sia
#from bs4 import BeautifulSoup
import BeautifulSoup
import requests
import re
#from google import google
import os, sys
import json
sys.path.append(os.path.dirname(__file__))
num_page = 1
def scrape(symbol) :
#	search_results = google.search(name + " ticker name", num_page)
#	symbol = search_results[0].name.split(' ')[0]
#	print symbol
	url = 'http://finance.yahoo.com/q?s={}'.format(symbol)
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")

	data = soup.find_all('p')
	
	return data       

def SentimentNews(name):    
	info = scrape(name)
	soup = BeautifulSoup(''.join(str(info)), "lxml")
	analyze = sia()
	dictionary = {}
	for span in soup.find_all('p'):
		score_dict = analyze.polarity_scores(span.text)
#		print score_dict
		dictionary[span.text] = str(score_dict)
	rp = json.dumps(dictionary)
	return rp

def GetStockNews(name):    
	info = scrape(name)
	soup = BeautifulSoup(''.join(str(info)), "lxml")
	analyze = sia()
	news = []
	for span in soup.find_all('p'):
		news.append(span.text.encode('utf-8'))
	return news



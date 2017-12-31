from bs4 import BeautifulSoup
import requests
import re
#from google import google
import os, sys
sys.path.append(os.path.dirname(__file__))
from lxml import html  
import requests
from exceptions import ValueError
from time import sleep
import json
import argparse
from collections import OrderedDict
from time import sleep
#from google import google
num_page = 1
def scrape(symbol) :
	url = 'http://finance.yahoo.com/q?s={}'.format(symbol)
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")

	data1 = soup.find_all('span', class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
	soup = BeautifulSoup(''.join(str(data1)), "lxml")
	data2 = soup.text
	return data2        
 
def parse(ticker):
	url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
	response = requests.get(url)
	sleep(4)
	parser = html.fromstring(response.text)
	summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
	summary_data = OrderedDict()
	other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
	summary_json_response = requests.get(other_details_json_link)
	json_loaded_summary =  json.loads(summary_json_response.text)
	y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
	earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
	eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
	datelist = []
	for i in earnings_list['earningsDate']:
		datelist.append(i['fmt'])
	earnings_date = ' to '.join(datelist)
	for table_data in summary_table:
		raw_table_key = table_data.xpath('.//td[@class="C(black)"]//text()')
		raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
		table_key = ''.join(raw_table_key).strip()
		table_value = ''.join(raw_table_value).strip()
		summary_data.update({table_key:table_value})
	summary_data.update({'1y Target Est':y_Target_Est,'EPS (TTM)':eps,'Earnings Date':earnings_date,'ticker':ticker,'url':url})
	return summary_data

def givelivedata(name):
	scraped_data = parse(name)
	dictionary = dict(scraped_data)
	dictionary['Stock_Value'] = scrape(name)
	rp = json.dumps(dictionary)
	return rp
	


if __name__=="__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('name',help = '')
	args = argparser.parse_args()
	name = args.name
#	print "Fetching data for %s"%(name)
	scraped_data = parse(name)
	dictionary = dict(scraped_data)
	dictionary['Stock_Value'] = scrape(name)
	rp = json.dumps(dictionary)
	print rp

from vaderSentiment import vaderSentiment
from news import news2
def getNewsSentiment(source):
	b = vaderSentiment.SentimentIntensityAnalyzer()
	news_list = news2.getNews(source)
	sentiment = 0
	for each in news_list:
		scores = b.polarity_scores(each)
		sentiment += (scores['pos'] - scores['neg'])

	return sentiment, news_list


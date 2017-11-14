import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd
import math
import quandl
import pickle
from sklearn.linear_model import ARDRegression , LinearRegression
import os, sys

sys.path.append(os.path.dirname(__file__))

quandl.ApiConfig.api_key = "DyJDeeYMoYiaSXzYzxjR"

shift = 1

def process (df) :
	df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) * 100 / df['Adj. Low']
	df['Change_PCT'] = (df['Adj. Close'] - df['Adj. Open']) * 100 / df['Adj. Open']
	# df = df[['Adj. Close','HL_PCT', 'Change_PCT', 'Adj. Volume']]
	df['HL_PCT'] = df['HL_PCT'] * 10

def preprocess_input(Open, High, Low, Close, Volume):
	# hl_pct = (High - Close) * 100 / Close
	# change_pct = (Close - Open) * 100 / Open
	ip = [Open, High, Low, Close, Volume]
	ipnum = np.array(ip)
	# ip = preprocessing.scale(ipnum)
	return ipnum

def getTrainedClassifier(ticker ,sd, ed, save = True) :
	df = quandl.get('WIKI/' + ticker, start_date = sd, end_date = ed)
	df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

	# df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) * 100 / df['Adj. Low']
	# df['Change_PCT'] = (df['Adj. Close'] - df['Adj. Open']) * 100 / df['Adj. Open']

	# df = df[['Adj. Close','HL_PCT', 'Change_PCT', 'Adj. Volume']]
	# df['HL_PCT'] = df['HL_PCT'] * 10

	df['future'] = df['Adj. Close'].shift(-shift)
	df.dropna(inplace=True)
	X_train = np.array(df.drop(['future'], 1))
	y_train = np.array(df['future'])


	# X = preprocessing.scale(X)
	# X_lately = X[-shift:]
	# X = X[:-shift]
	# y = y[:-shift]
	# X_train, X_test = cross_validation.train_test_split(X,  test_size = 0.0)
	# y_train, y_test = cross_validation.train_test_split(y, test_size = 0.0)
	# p = preprocess_input(  799.70  ,  801.670 , 795.2501   ,   801.34  ,  1161986.0)
	# p1 = preprocess_input(135.10,135.83,135.10,135.6900,21976977)

	clf = ARDRegression()
	clf.fit(X_train, y_train)
	return clf

def getTrendPredictions(clf, ticker, sd, ed):
	df1 = quandl.get('WIKI/' + ticker, start_date = sd , end_date = ed)	
	df1 = df1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
	df1['future'] = df1['Adj. Close'].shift(-shift)
	df1.dropna(inplace=True)
	X_test = np.array(df1.drop(['future'], 1))
	y_test = np.array(df1['future'])
	
	predictions = clf.predict(X_test)
	i = 0
	delta = 0
	while i < len(predictions) - 1:
		delta += predictions[i + 1] - predictions[i]
		i += 1
		
	return delta
	
'''
clf = getTrainedClassifier('GOOG',"2010-02-12","2017-02-5")

df1 = quandl.get('WIKI/GOOG', start_date = "2017-02-6" , end_date = "2017-02-20")
df1 = df1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# process(df1)


df1['future'] = df1['Adj. Close'].shift(-shift)
df1.dropna(inplace=True)
X_test = np.array(df1.drop(['future'], 1))
y_test = np.array(df1['future'])

accuracy = clf.score(X_test, y_test)
print accuracy
print clf.predict(X_test) '''

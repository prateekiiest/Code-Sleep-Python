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
	df['HL_PCT'] = df['HL_PCT'] * 10

def preprocess_input(Open, High, Low, Close, Volume):
	ip = [Open, High, Low, Close, Volume]
	ipnum = np.array(ip)
	return ipnum

def getTrainedClassifier(ticker ,sd, ed, save = True) :
	df = quandl.get('WIKI/' + ticker, start_date = sd, end_date = ed)
	df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
	df['future'] = df['Adj. Close'].shift(-shift)
	df.dropna(inplace=True)
	X_train = np.array(df.drop(['future'], 1))
	y_train = np.array(df['future'])
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

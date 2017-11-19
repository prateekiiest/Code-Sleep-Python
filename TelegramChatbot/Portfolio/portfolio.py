import MySQLdb
from yahoo_finance import Share
db = MySQLdb.connect("localhost", "root", "root", "chatbot")
cursor = db.cursor()

def insert_stock(ticker, quantity, buying_price):
	query = "insert into portfolio values('" + ticker + "', " + str(quantity) + " , "+ str(buying_price) + ")"
	try:
		cursor.execute(query)
		db.commit()
		return True
	except:
		return False

def stop_service():
	db.close()

def calculate_profit():
	query = "select * from portfolio"
	cursor.execute(query)
	results = cursor.fetchall()
	profit = 0.00
	for t in results:
		ticker = t[0]
		quantity = int(t[1])
		buyrate = float(t[2])
		share = Share(t[0])
		current_price = float(share.get_price())
		profit += (current_price - buyrate) * quantity
	return profit

def remove(ticker):
	query = "delete from portfolio  where stock_ticker = " + ticker 
	try:
		cursor.execute(query)
		db.commit()
		return True
	except:
		return False

def showPortfolio():
	query = "select * from portfolio"
	cursor.execute(query)
	results = cursor.fetchall()
	string = ''
	for t in results:
		string += t[0] + " Buying Price : " + str(t[2]) + " No. Of Shares : " + str(t[1]) + "\n\n"
	return string

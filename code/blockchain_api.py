import requests,json
url = "https://blockchain.info/ticker"
result = requests.get(url)
data = result.json()
row = (data['USD'])
sell = row['sell']
price = row['last']
buy = row['buy']
symbol = row['symbol']
print "Source:blockchain"
print "most recent market price:%s%.2f" % (symbol,price)
print "Sell:%s%.2f" % (symbol,sell)
print "buy:%s%.2f" % (symbol,buy)
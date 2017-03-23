import requests,json
import sys,csv

def capdata(fileName):
	csvfile = file(fileName,'a')
	writer = csv.writer(csvfile)
	url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-01-01&end=2017-03-22"
	result = requests.get(url)
	data = result.json()
	bpi = (data['bpi'])

	for key in bpi.keys():
		htime = key
		price = bpi[key]
		data = [htime,price]
		writer.writerow(data)

	csvfile.close()

#main
capdata('history_price.csv')
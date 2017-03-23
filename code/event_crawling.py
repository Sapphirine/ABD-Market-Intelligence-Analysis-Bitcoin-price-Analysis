# -*- coding: utf-8 -*-
import urllib2
import re
import pickle
from datetime import datetime
import os.path
import csv,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def May_to_5(month_word):
	return{
		'January':1,
		'February':2,
		'March':3,
		'April':4,
		'May':5,
		'June':6,
		'July':7,
		'August':8,
		'September':9,
		'October':10,
		'November':11,
		'December':12,
	}[month_word]

def capdata(fileName):
	url = "https://99bitcoins.com/price-chart-history/"
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	headers = {'User-Agent':user_agent}
	request = urllib2.Request(url=url,headers=headers)
	try:
		response = urllib2.urlopen(request)
	except urllibs.URLError, e:
		print e.reason
	except urllib2.HTTPError, e:
		print e.code
	else:
		print "OK"
#print response.read()

	csvfile = file(fileName,'a')
	writer = csv.writer(csvfile)
	content = response.read().decode('utf-8')
	pattern = re.compile('<h3>(.*?)\s-\s(.*?)</h3>',re.S)
	items = re.findall(pattern,content)

	for item in items:
		event = item[0]
		date1 = item[1].split(' ')
		month_word = date1[0]
		month = int(May_to_5(month_word))
		day = int(date1[1][0])
		year = int(date1[2])
		#time = datetime(int(year),int(month),int(day))
		etime = str(year)+'-'+str(month)+'-'+str(day)
		data = [event,etime]
		writer.writerow(data)

	csvfile.close()

#main
#for i in range(ITERATIONS):
capdata('event.csv')
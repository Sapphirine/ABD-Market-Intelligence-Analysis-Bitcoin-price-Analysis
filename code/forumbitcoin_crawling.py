# -*- coding: utf-8 -*-
import urllib2
import re
import pickle
from datetime import datetime
import os.path
import csv,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

PAGE = 14

def May_to_5(month_word):
	return{
		'Jan':1,
		'Feb':2,
		'Mar':3,
		'Apr':4,
		'May':5,
		'Jun':6,
		'Jul':7,
		'Aug':8,
		'Sep':9,
		'Oct':10,
		'Nov':11,
		'Dec':12,
	}[month_word]

def pm_to_21(hour,ampm):
	if ampm == 'am':
		return hour
	elif ampm == 'pm':
		hour = hour+12
		return hour

def capdata(fileName,url):
	url = "https://forum.bitcoin.com/press/page"+url+".html"
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	headers = {'User-Agent':user_agent}
	request = urllib2.Request(url=url,headers=headers)
	try:
		response = urllib2.urlopen(request)
	except urllib2.URLError, e:
		print e.reason
	except urllib2.HTTPError, e:
		print e.code
	else:
		print "OK"

	csvfile = file(fileName,'a')
	writer = csv.writer(csvfile)
	content = response.read().decode('utf-8')
	pattern_title = re.compile(r'class=\"topictitle\">(.*?)</a>')
	pattern_time = re.compile(r'</i></a>\s<br\s/>(.*?)</span>')
	titles = re.findall(pattern_title,content)
	times = re.findall(pattern_time,content)

	for i in range(2,len(titles)-1):
		title_time = titles[i]
		s_title = title_time.split(']')
		if len(s_title)<2:
			title = title_time
		else:
			title = s_title[1]

		s = times[i].split(' ')
		month_word = s[1]
		day_comma = s[2]
		day = day_comma.split(',')[0]
		year = s[3]
		hourmin = s[4]
		ampm = s[5]
		month = May_to_5(month_word)
		s_hourmin = hourmin.split(':')
		temp = int(s_hourmin[0])
		hour = pm_to_21(temp,ampm)
		minute = s_hourmin[1]
		ctime = str(year)+'-'+str(month)+'-'+str(day)+' '+str(hour)+':'+str(minute)+':00'

		data = [title,ctime]
		writer.writerow(data)

	csvfile.close()

#main
for i in range(0,PAGE):
	count = 50*i
	if count == 0:
		url = '00'
	else:
		url = str(count)
	capdata('fourumbitcoin.csv',url)
	print i
	time.sleep(10)

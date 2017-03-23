# -*- coding: utf-8 -*-
import urllib2
import re
import pickle
from datetime import datetime,date
import os.path
import csv,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

PAGE = 827

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

def pm_to_21(hour,ampm):
	if ampm == 'AM':
		return hour
	elif ampm == 'PM':
		hour = hour+12
		return hour

def capdata(fileName,url):
	url = "https://bitcointalk.org/index.php?board=1."+url
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
	content = response.read().decode('ISO-8859-1')
	#print content
	pattern_title = re.compile(r'"><a\shref=\"https://bitcointalk\.org/index\.php\?topic=(.*?)\">(.*?)</a>')
	pattern_time = re.compile(r'title=\"Last(.*?)smalltext\">\s(.*?)by',re.DOTALL)
	pretitles = re.findall(pattern_title,content)
	pretimes = re.findall(pattern_time,content)
	times = []
	for pretime in pretimes:
		s = pretime[1].split('\t\t\t\t\t\t\t\t')
		ss = s[1].split('<br')[0]

		all = ss.split(' ')
		if all[0] == '<b>Today</b>':
			today = str(date.today());
			prehms = all[2]
			hms = prehms.split(':')
			temp = int(hms[0])
			minute = hms[1]
			second = hms[2]
			ampm = all[3]
			hour = pm_to_21(temp,ampm)
			ctime = today + ' '+ str(hour)+':'+str(minute)+':'+str(second)
		else:
			month_word = all[0]
			month = May_to_5(month_word)
			day = all[1].split(',')[0]
			year = all[2].split(',')[0]
			prehms = all[3]
			hms = prehms.split(':')
			temp = int(hms[0])
			minute = hms[1]
			second = hms[2]
			ampm = all[4]
			hour = pm_to_21(temp,ampm)
			ctime = str(year)+'-'+str(month)+'-'+str(day)+' '+str(hour)+':'+str(minute)+':'+str(second)
		#print type(ctime)
		times.append(ctime)

	#print len(times)
	titles = []
	for pretitle in pretitles:
		title = str(pretitle[1])
		titles.append(title)

	for i in range(0,len(titles)):
		title = titles[i]
		ctime = times[i]
		data = [title,ctime]
		writer.writerow(data)
	csvfile.close()

#main

for i in range(0,PAGE):
	count = 40*i
	if count == 0:
		url = '00'
	else:
		url = str(count)
	capdata('bitcointalk.csv',url)
	print i
	time.sleep(5)

#capdata('bitcointalk.csv','00')


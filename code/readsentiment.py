import csv
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

with open('bitcointalkn.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    #writer=csv.write(c)

    column=[]
    result=[]
    for row in reader:
        column.append(row[0])

    for line in column:
    	print line
    	blob=TextBlob(line,analyzer=NaiveBayesAnalyzer())
    	#res=str(blob.sentiment[1])
    	result=(str(blob.sentiment[1]))
    	print result
    	with open('new.csv', 'wb') as f:
    		writer = csv.writer(f)
    		for row in reader:
    			row.append(result)
    			print row
                writer.writerow(row)
  

    	        f.close()
    	#result.append(",")
csvfile.close()


    	
    

        #c=open("url.csv","w")
        #writer=csv.write(c)
        #writer.writerow(['name','address','city','state'])


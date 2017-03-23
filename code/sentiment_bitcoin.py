from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

sentence='Bitcoin Sign Accepted into Unicode'

blob=TextBlob(sentence,analyzer=NaiveBayesAnalyzer())
print (blob.sentiment)
print ("The sentiment result:" +str(blob.sentiment[1]/blob.sentiment[2]))
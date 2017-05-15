import os
import numpy as np
import csv
from sklearn.preprocessing import StandardScaler, Imputer

def data_pre(type):

        if (type=='train'):
		data=np.load('data/train_data16.npy')
		label=np.load('data/train_label.npy')
	else:
		data=np.load('data/test_data16.npy')
		label=np.load('data/test_label.npy')

	days=35
	step=1
	lstm_data=[]
	lstm_label=[]
	count=0
 
	for i in range(0,len(data)-step-days):
		if (count==step):
			
			lstm_data.append(data[i:i+days,:])
			lstm_label.append(label[i])
			count=0
		count+=1

  
	return np.array(lstm_data), np.array(lstm_label)





if __name__ == '__main__':
    data_pre('test')

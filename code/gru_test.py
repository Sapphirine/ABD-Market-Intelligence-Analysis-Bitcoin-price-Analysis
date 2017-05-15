import numpy as np

import tensorflow as tf

from data_analysis import data_pre
import sys
sys.path.insert(0,'/home/lpy/tflearn/')
import tflearn


train_data,train_label = data_pre('train')
test_data,test_label = data_pre('test')
print train_data.shape
print test_data.shape
days=35

net = tflearn.input_data(shape=[None, days, 21])
net = tflearn.gru(net, 40, return_seq=False)#,dropout=0.8)
net = tflearn.dropout(net, 0.8)

#net = tflearn.lstm(net, 512)#,dropout=0.8)
#net = tflearn.dropout(net, 0.8)

net = tflearn.fully_connected(net, 1, activation='linear')
net = tflearn.regression(net, optimizer='rmsprop', loss='mean_square',metric='R2', name="target")

model = tflearn.DNN(net)
#model.fit(train_data, train_label, n_epoch=10000,run_id='lstm',snapshot_epoch=True,validation_set=(test_data,test_label), show_metric=True, batch_size=20)
#model.save("model/bitcoin_lstm.tfl")
#model.load("model/-53041")
model.load("model_gru/-29205")
print model.predict(test_data),test_label
p= model.predict(test_data)
np.save('predict_price_gru',p)


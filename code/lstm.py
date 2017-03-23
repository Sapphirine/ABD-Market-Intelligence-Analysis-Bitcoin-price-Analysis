import numpy as np
import tensorflow as tf

from data_analysis import new_data_pre
import sys
sys.path.insert(0,'/home/lpy/tflearn/')
import tflearn

train_data,train_label = new_data_pre(type='train')
test_data,test_label = new_data_pre(type='test')
print train_data.shape
print train_label.shape

net = tflearn.input_data(shape=[None, 30, 10])
net = tflearn.lstm(net, 10, return_seq=True)
net = tflearn.dropout(net, 0.8)

net = tflearn.lstm(net, 10)
net = tflearn.dropout(net, 0.8)

net = tflearn.fully_connected(net, 1, activation='linear')

#rmsprop=tflearn.RMSProp(learning_rate=0.01, decay=0.95)
net = tflearn.regression(net, optimizer='adam',
                          loss='mean_square',metric=r2, name="output1")

model = tflearn.DNN(net, tensorboard_verbose=2,tensorboard_dir='/tensorflow/log/',checkpoint_path='model/lstm/')
model.fit(train_data, train_label, n_epoch=150,run_id='lstm',snapshot_epoch=True,validation_set=(test_data,test_label), show_metric=True,batch_size=20)
model.save("model/lstm.tfl")


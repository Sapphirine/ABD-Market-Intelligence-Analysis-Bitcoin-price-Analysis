# -*- coding: utf-8 -*-
import scipy.io as scio
import numpy as np

def read_mat(XFile,YFile):
	X_dict = scio.loadmat(XFile)
	Y_dict = scio.loadmat(YFile)
	X_set = np.ndarray.tolist(X_dict['X_set'])
	Y_set = np.ndarray.tolist(Y_dict['Y_set'])
	# one row in X_set: X_set[i]
	# visit the element on ith row and jth column: X_set[i][j]
	return X_set,Y_set


if __name__=="__main__":
	XFile = '***/X_set_0510.mat'   # *** is the absolute path of X_set_XXXX.mat
	YFile = '***/Y_set_0510.mat'   # *** is the absolute path of Y_set_XXXX.mat
	[X_set,Y_set] = read_mat(XFile,YFile)
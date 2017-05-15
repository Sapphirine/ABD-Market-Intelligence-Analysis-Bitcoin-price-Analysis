import numpy as np
import xlwt

predict_data=np.load("predict_price16_gru.npy")
original_data=np.load("test_label.npy")
price=[]
pp=[]
for p in original_data:
    price.append(p)
for k in predict_data:
    pp.append(k)
price.reverse()
pp.reverse()

dif=len(price)-len(pp)
for l in range(dif):
	price.pop(0)
print price[100]
print "pause"
print pp[100]

'''for i in range(0,len(p)-1):
	c=p[i][0]
	cc=g[i+37][0]
	print c
	print cc'''



wbk = xlwt.Workbook()
sheet = wbk.add_sheet('predict_price')
sheet2= wbk.add_sheet('gorund_truth')
# indexing is zero based, row then column

for j in range(0,len(pp)-1):
	sheet.write(j,0,pp[j][0])
	#print pp[j][0]

for i in range(0,len(price)-1):
	sheet2.write(i,0,price[i][0])

wbk.save('price_gru16.xls')

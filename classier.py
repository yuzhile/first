import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.ensemble import ExtraTreesClassifier as eclf
x = np.loadtxt('extration.csv',delimiter=',')

y = np.loadtxt('label.csv',delimiter=',')

x = preprocessing.scale(x)
#clf = svm.SVC()
clf = eclf(n_estimators=30)
params = clf.fit(x,y)
result = clf.predict(x)
print params 
count = 0
buy = 0
for i in range(len(y)):
	if result[i] == 1 and y[1] == 1:
		print i
		count = count + 1
	if y[i] == 1:
		buy =  buy + 1
	
print count
print buy

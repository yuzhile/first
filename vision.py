import numpy as Math
import pylab as Plot
import csv
from tsne import bh_sne
from sklearn import preprocessing
X = Math.loadtxt("extration.csv",delimiter=",");
label = Math.loadtxt("label.csv",delimiter=",");
#X = Math.loadtxt("newdata.csv",delimiter=",",dtype=float);
X = preprocessing.scale(X)
#labels = Math.loadtxt("label.csv",delimiter=",",dtype=str);
#Y = bhtsne.bh_tsne(X);
Y = bh_sne(X,perplexity=45);
rf = file('rf.csv','wb')
rw = csv.writer(rf)
for y in Y:
	rw.writerow(y)
Plot.scatter(Y[:,0], Y[:,1],20,label);
#tsne.Plot.scatter(Y[:,0], Y[:,1], 20);
Plot.show()

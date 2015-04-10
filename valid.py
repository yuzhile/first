import csv
import numpy as np
def loadParamter(paramterfile):
	parafile = file(paramterfile)
	reader = csv.reader(parafile)
	paramter = reader.next()
	lparamter = [0 for i in range(len(paramter)+1)]
	i = 0
	for l in paramter:
		lparamter[i] = int(l)
		i = i+1
	psum = sum(lparamter)
	i = 0
	for p in lparamter:
		lparamter[i] = (p/(psum*1.0))
		i = i+1

	return lparamter
def calScore(w,paramter):
	score = 0
	#i = 0
	for i in range(len(w)):
		score = score + float(w[i]) * paramter[i]
	return score	
def getScore(paramter):
	extration_file = file('extration.csv')
	lable_file = file('label.csv')
	e_reader = csv.reader(extration_file)
	l_reader = csv.reader(lable_file)

	scores = []
	for w in e_reader:
		scores.append(calScore(w,paramter))
	
	npscores = np.array(scores)
	#print type(npscores[0])
	argscores = np.argsort(-npscores)

	buy = []
	i = 0
	for j in l_reader:
	#	if 1 == int(j[0]):
	#		buy.append(i)
		buy.append(j)

		i = i + 1

	count = 0
	for i in range(50000):
		#if argscores[i] in buy:
		#	count  = count + 1
		#print scores[argscores[i]]
		print buy[argscores[i]][0]+','+buy[argscores[i]][1]
		i = i+ 1
	#print count,len(buy)
	#p =  count / (len(buy) * 1.0)	
	#c =  count / (1.0*50000)
	#f = 2*p*c/(p+c)
	#print p,c,f
if __name__ == '__main__':
	paramter = loadParamter('time_weight.csv')
	
	print 'user_id,item_id'
	#print paramter
	getScore(paramter)

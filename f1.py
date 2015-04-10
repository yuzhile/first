import csv
from sets import Set

if __name__ == '__main__':
	predictfile = file('clearresult.csv')
	resultfile = file('predict.csv')
	readerp = csv.reader(predictfile)
	readerr = csv.reader(resultfile)
	
	predict = Set()
	result = Set()
	for p in readerp:
		predict.add((p[0]))
	for r in readerr:
		result.add((r[0]))

	common = predict.intersection(result)
	if 0 == len(common):
		print len(predict),len(result),len(common)
	else:
		print len(predict)
		print len(result)
		print len(common)
		precision = len(common) / (1.0*len(predict))
		recall = len(common) / (1.0*len(result))
		f1 = 2*precision*recall / (precision+recall)
		print precision,recall,f1
	

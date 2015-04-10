import csv

resultfile = file('result.csv')
result = csv.reader(resultfile)

for r in result:
	if r[0][0] != '[':
		#temp = []
		#temp.append(r)
		print r[0]

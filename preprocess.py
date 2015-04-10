import csv
import numpy as np
def dateNum(date):
	parts = date.split()
	time = parts[0].split('-')
	if(11 == int(time[1])):
		return int(time[2]) - 17
	else:	
		return 13+int(time[2])
sourcefile=file('train_user.csv','rb')
destfile=file('user_test.csv','wb')
reader=csv.reader(sourcefile)
writer=csv.writer(destfile)
#x = np.loadtxt('train_user.csv',delimiter=",",dtype='int,int,int,str,int,str')
#z = zip(x[:,0],x[:,-1])
#np.savetxt('train_after.csv',z,delimiter=',')	
#print len(x)	
#days = ['2014-11-18 00','2014-11-19 00','2014-11-20 00',
#	'2014-11-21 00','2014-11-22 00','2014-11-23 00','2014-11-24 00','2014-11-25 00',
#	'2014-11-26 00','2014-11-27 00','2014-11-28 00','2014-11-29 00','2014-11-30 00',
#	'2014-12-01 00','2014-12- 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-11-12 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-12-18 00','2014-11-18 00','2014-12-18 00','2014-12-18 00','2014-12-18 00']

i = 0
temp = []
for row in reader:
	temp = []
	#temp.append(row[0])
	#temp.append(row[-1])
	temp = row[0:3]
	temp.append(row[4])
	#date = row[-1]
	temp.append(dateNum(row[5]))
	writer.writerow(temp)
	if 100000 == i:
		break	
	i = i+1

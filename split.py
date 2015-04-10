import train
import csv
def test():
	print 'test'
if __name__ == '__main__':
	command = 'select * from train_user'
	curor = train.connectDb(command)
	recommendfile = file('predict.csv','wb')
	testfile = file('testfile','wb')
	wr = csv.writer(recommendfile)
	wt = csv.writer(testfile)
	for data in curor.fetchall():
		if data[-1] == 31:
			#temp = []
			if train.isBuy(data[2]):
				temp = data[0:2]
				wr.writerow(temp)
		else:
			wt.writerow(data)	

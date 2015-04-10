import MySQLdb as db
import csv

def isBuy(itemType):
	if 4==itemType:
		return True
def statsBuy(action,paramter,userinfo,buyitem):
	keys = buyitem.keys()
	for item in keys:
		for user in userinfo:
			if item == user[1]:
				if user[-1] <= buyitem[item]:
					index = buyitem[item]-user[-1]
#					print index
					paramter[index] = paramter[index] + 1
					action[user[2]] = action[user[2]] + 1



def connectDb(command):
	'''
		input:command is the command executed by sql	
		output :the rusult executed by sql,it is curor of the db
	'''
	cxn = db.connect(host='localhost',db='albb',user='root',passwd='root')
	curor = cxn.cursor()
	#result = curor.execute('select * from test_user order by user_id limit 10000')
	result = curor.execute(command)
	return curor

def max_time(x,y):
	if x < y:
		return y
	else:
		return x
def learnParamter(curor):
	'''
		output:p[0,1,...,30]
			a[0,1,2,3]
	'''
	newuser= False
	pre = -1
	cur = 0
	userinfo = []
	buyitem = {} 
	paramter = [i*0 for i in range(31)]
	actionbuy = [i*0 for i in range(5)]
	actioncommon = [i*0 for i in range(5)]
	waction = [i*0 for i in range(5)]
	for data in curor.fetchall():
		cur = data[0]
		actioncommon[data[2]] = actioncommon[data[2]] + 1
		if cur != pre:
		#	newuser = True
			if 0 != len(buyitem): 
				statsBuy(actionbuy,paramter,userinfo,buyitem)
			userinfo = []
			buyitem = {}
		userinfo.append(data)
		if isBuy(data[2]):
			#temp = []
			#temp.append(data[1])
			#temp.append(data[-1])
			if buyitem.has_key(data[1]):
				buyitem[data[1]] = max_time(data[-1],buyitem[data[1]])
			else:
				buyitem[data[1]] = data[-1]	
			#buyitem.append(temp)
	
		pre = data[0]
	statsBuy(actionbuy,paramter,userinfo,buyitem)
	print paramter
	for i in range(5):
		if 0 != i:
			waction[i] = actionbuy[i] / (1.0 * actioncommon[i])
	destfile=file('paramter.csv','wb')
	writer = csv.writer(destfile)
	writer.writerow(paramter)
	writer.writerow(actionbuy)
	writer.writerow(actioncommon)
	writer.writerow(waction)
if __name__ == '__main__':
	command = 'select * from train_user order by user_id' 
	curor = connectDb(command)
	learnParamter(curor)	

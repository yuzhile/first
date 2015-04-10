import MySQLdb as db
import csv
import numpy as np
def isBuy(itemType):
	if 4==itemType:
		return True
def gettimeItem(userinfo,timeItems):
	for user in userinfo:
		temp = []
		if timeItems.has_key(user[-1]):
			timeItems[user[-1]].append(user[3])
		else:
			temp.append(user[3])
			timeItems[user[-1]] = temp
def getValue(weight,action,timeItem,user):
	pre = timeItem.count(user[3])/(1.0*len(timeItem))
	lw = 31 - int(user[-1])
	
	
#	print time
	#print weight,action
	#return weight[lw]*action[user[2]]*pre
	return weight[lw]*action[user[2]]
def insertScore(scores,item_id,value):
	if scores.has_key(item_id):
		scores[item_id] = scores[item_id] + value
	else:
		scores[item_id] = value

def rateScore(user_id,scores,writer):
	values = scores.values()
	npvalues = np.array(values)
	argvalues = np.argsort(-npvalues)
#	print argvalues
#	print scores.keys()
	keys = scores.keys()
	#print len(keys)
	if 0 == len(keys):
		return
	i = 0
	line = []
#	for  key in keys:
#		if scores[key] >= 10:
#			print user_id,key	
#		else:
#			print values[arg]
			#print scores[key]
	#	line = []
	#	writer.writerow(scores[key])
	for i in range(10):
		if i < len(keys):
			print '%d,%d'%(user_id,keys[argvalues[i]])
	#	line = []
	#	line.append(user_id)
	#	line.append(keys[argvalues[i]])
		#line.append(values[argvalues[i]])
	#	writer.writerow(line)
		#print line
	
	#print user_id,keys[argvalues[0]],values[argvalues[0]]	
def max_time(x,y):
	if x < y:
		return y
	else:
		return x


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

def getScore(weight,action,userinfo,buyitem,writer):
#	scores = [i*0 for i in range(10)]

	timeItems = {}
	
	scores = {}
	gettimeItem(userinfo,timeItems)
	user_id = 0
	item_keys = buyitem.keys()
	for user in userinfo:
		if user[1] in item_keys:
			continue
		else:
			timeItem = timeItems[user[-1]]
			value = getValue(weight,action,timeItem,user)
			insertScore(scores,user[1],value)
			user_id = user[0]
			#print scores.keys()
#	print scores.keys()
	rateScore(user_id,scores,writer)	



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
		#lparamter[i] = 100*(p/(psum*1.0))
		i = i+1
	action = reader.next()
	#laction = [i*0 for i in range(len(action)+1)]
	laction = [0 for i in range(len(action)+1)]

	i = 0
	for l in action:
		#laction[i] = float(l)* 10.0
		laction[i] = float(l)
		i = i+1
		
	return lparamter,laction
def train(curor,paramterfile):
	'''
		output:p[0,1,...,30]
			a[0,1,2,3]
	'''

	
	weight,action = loadParamter(paramterfile)

	#print weight,action
	pre = -1
	cur = 0
	userinfo = []
	buyitem = {} 
	
	destfile=file('recommender.csv','wb')
	writer = csv.writer(destfile)
	#writer.writerow('user_id,item_id')
	

	for data in curor.fetchall():
		cur = data[0]
		#actioncommon[data[2]] = actioncommon[data[2]] + 1
		if cur != pre:
			getScore(weight,action,userinfo,buyitem,writer)
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
	
		pre = cur
	getScore(weight,action,userinfo,buyitem,writer)
	#destfile=file('recommender.csv','wb')
	#writer = csv.writer(destfile)
	#writer.writerow(paramter)
	#writer.writerow(actionbuy)
	#writer.writerow(actioncommon)
	#writer.writerow(waction)
if __name__ == '__main__':
	command = 'select * from train_user order by user_id,item_id ' 
	curor = connectDb(command)
	paramterfile = 'time_weight.csv'
	print 'user_id,item_id'
	train(curor,paramterfile)	

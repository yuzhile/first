import MySQLdb as db
import csv
import numpy as np
def isBuy(itemType):
	if 4==itemType:
		return True
def learnParamter(paramter,userinfo,buyitem):
	for user in userinfo:
		for item in buyitem:
			if item[0] == user[1]:
				if user[-1] <= item[1]:
					index = item[1]-user[-1]
#					print index
					#paramter[index] = paramter[index] + 1
def gettimeItem(userinfo,timeItems):
	for user in userinfo:
		temp = []
		if timeItems.has_key(user[-1]):
			timeItems[user[-1]].append(user[3])
		else:
			temp.append(user[3])
			timeItems[user[-1]] = temp
def getValue(weight,timeItem,catory,time):
	pre = timeItem.count(catory)/(1.0*len(timeItem))
	lw = 32 - int(time)
	
#	print time
	return weight[lw]*pre
def insertScore(scores,item_id,value):
	if scores.has_key(item_id):
		scores[item_id] = scores[item_id] + value
	else:
		scores[item_id] = value

def rateScore(user_id,scores):
	values = scores.values()
	npvalues = np.array(values)
	argvalues = np.argsort(-npvalues)
#	print argvalues
#	print scores.keys()
	keys = scores.keys()
	if 0 == len(keys):
		return
	print user_id,keys[argvalues[0]],values[argvalues[0]]	
def getScore(weight,userinfo,buyitem):
#	scores = [i*0 for i in range(10)]
	timeItems = {}
	
	scores = {}
	gettimeItem(userinfo,timeItems)
	user_id = 0
	for user in userinfo:
		if user in buyitem:
			continue
		else:
			timeItem = timeItems[user[-1]]
			value = getValue(weight,timeItem,user[3],user[-1])
			insertScore(scores,user[1],value)
			user_id = user[0]
			#print scores.keys()
#	print scores.keys()
	rateScore(user_id,scores)	
# connect mysql

 		
cxn = db.connect(host='localhost',db='albb',user='root',passwd='root')
curor = cxn.cursor()
#result = curor.execute('select * from test_user order by user_id limit 10000')
result = curor.execute('select * from test_user order by user_id ')
#result = curor.execute('select * from train_user order by user_id ')


parafile=file('paramter.csv')
reader=csv.reader(parafile)
paramter = reader.next()
lparamter = [i*0 for i in range(31)]
j = 0
for l in paramter:
	
	lparamter[j] = int(l)
	j = j + 1
	
weight = [i*0 for i in range(32)]
#print lparamter
psum = sum(lparamter)
j = 0
for p in lparamter:
	weight[j] = p/(psum*1.0)
	j = j + 1
#print weight	
#paramter = [i*0 for i in range(31)]


newuser= False
pre = -1
cur = 0
userinfo = []
buyitem = []
buys = []

for data in curor.fetchall():
	cur = data
	if cur[0] != pre:
		newuser = True
		
		getScore(weight,userinfo,buyitem)
		userinfo = []
		buyitem = []
	userinfo.append(cur)
	if isBuy(cur[2]):
	#	temp = []
	#	temp.append(cur[1])
	#	temp.append(cur[-1])
		buyitem.append(cur[1])
	
	pre = cur[0]
#learnParamter(paramter,userinfo,buyitem)
#print paramter

#destfile=file('paramter.csv','wb')
#writer = csv.writer(destfile)
#writer.writerow(paramter)

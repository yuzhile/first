import MySQLdb as db
import csv
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
					paramter[index] = paramter[index] + 1

cxn = db.connect(host='localhost',db='albb',user='root',passwd='root')
curor = cxn.cursor()
#result = curor.execute('select * from test_user order by user_id limit 10000')
result = curor.execute('select * from test_user order by user_id ')
#result = curor.execute('select * from train_user order by user_id ')


newuser= False
pre = -1
cur = 0
userinfo = []
buyitem = []
paramter = [i*0 for i in range(31)]
for data in curor.fetchall():
	cur = data
	if cur[0] != pre:
		newuser = True
		if 0 != len(buyitem): 
			learnParamter(paramter,userinfo,buyitem)
		userinfo = []
		buyitem = []
	userinfo.append(cur)
	if isBuy(cur[2]):
		temp = []
		temp.append(cur[1])
		temp.append(cur[-1])
		buyitem.append(temp)
	
	pre = cur[0]
learnParamter(paramter,userinfo,buyitem)
print paramter

destfile=file('paramter.csv','wb')
writer = csv.writer(destfile)
writer.writerow(paramter)

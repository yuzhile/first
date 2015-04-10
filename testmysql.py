import MySQLdb as db
import csv

predictfile = file('predict.csv')
readerp = csv.reader(predictfile,delimiter=',')
items = []
for p in readerp:
	items.append(int(p[1]))
#print items
cxn = db.connect(host='localhost',db='albb',user='root',passwd='root')
cur = cxn.cursor()
#result = cur.execute('select * from ain_item where item_id=251151361')
result = cur.execute('select * from test_user order by user_id limit 100000')

i = 0
for data in cur.fetchall():
	if data[-1] <= 30 and data[1] in items:
		print data
		i = i+1
#	print data[0,4]
#print i / (1.0 * len(items)) 
#	print data[0]
#	print data[1]

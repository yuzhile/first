import MySQLdb as sql

#createtable1 = 'create table train_item(item_id int,item_geohash char(20),item_category int)'
createtable1 = 'create table train_item(item_id int,item_category int)'
loadcommand='load data infile \'testfile\' into table scores character set utf8  fields terminated by \',\' enclosed by \'\"\' lines terminated by \'\r\n\''
print loadcommand
cxn = sql.connect(host='localhost',db='albb',user='root',passwd='root')
cur = cxn.cursor()
#cur.execute(createtable1)
cur.execute(loadcommand)

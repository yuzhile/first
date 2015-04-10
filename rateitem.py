import train
import csv

def getPredict(f):
	predict_file = file(f)
	p_reader = csv.reader(predict_file)
	
	predict = []
	for p in p_reader:
		predict.append(int(p[1]))	
	return predict
def insertFeature(features,data,action):
	if features.has_key(data[1]):
		features[data[1]][31-data[-1]] = action[data[2]] + features[data[1]][31-data[-1]] 
	else:
		time = [0 for i in range(32)]
		time[31-data[-1]] = action[data[2]]
		features[data[1]] = time

def getFeature(userinfo,buyitem,feature,action):

	for user in userinfo:
		if user[1] in buyitem:
			continue
		insertFeature(feature,user,action)
def genLabel(features,predict):
	keys = features.keys()
	label = []
	for key in keys:
		if key in predict:
			label.append(1)
		else:
			label.append(0)
	#print 'l len:',len(label),len(features)
	return label
def output(user_id,features,r_writer,l_writer):
	keys = features.keys()
	i = 0
	for key in keys:
		temp = []
		r_writer.writerow(features[key])
		temp.append(user_id)
		temp.append(key)
		l_writer.writerow(temp)
		i = i+1	
def loadParamter(paramterfile):
	parafile = file(paramterfile)
	reader = csv.reader(parafile)
	action = reader.next()
	#laction = [i*0 for i in range(len(action)+1)]
	laction = [0 for i in range(len(action)+1)]

	i = 0
	for l in action:
		laction[i] = float(l)
		i = i+1
		
	return laction

def extration(curor,predict_file,result_file,label_file):
	
	pre = -1
	cur = 0
	
	#predict = getPredict(predict_file)

	r_file = file(result_file,'wb')
	r_writer = csv.writer(r_file)

	l_file = file(label_file,'wb')
	l_writer = csv.writer(l_file)
	
	
	features = {}
	
#	label = []
	
	action = loadParamter('action.csv')

	userinfo = []
	buyitem = []

	#print predict
	for data in curor.fetchall():
		cur = data[0]
	#	print data
		if cur != pre:
			
			getFeature(userinfo,buyitem,features,action)
#			label = genLabel(features,predict)
			output(data[0],features,r_writer,l_writer)
			features = {}	
			userinfo = []
			buyitem = []
#			label = []
		userinfo.append(data)
		if train.isBuy(data[2]):
			buyitem.append(data[1])
		pre = cur
	getFeature(userinfo,buyitem,features,action)
#			label = genLabel(features,predict)
	output(data[0],features,r_writer,l_writer)
		
if __name__ == '__main__':
	command = 'select * from train_user order by user_id ,item_id '
	curor = train.connectDb(command)
	
	result_file = 'extration.csv'
	
	predict_file = 'predict.csv'

	label_file = 'label.csv'
	extration(curor,predict_file,result_file,label_file)
	

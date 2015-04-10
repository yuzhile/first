import csv

l_file = file('label.csv')

l_reader = csv.reader(l_file)

count = 0
for l in l_reader:
	if 1== int(l[0]):
		count = count+1
print count

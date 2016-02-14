import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

xlist = []
rows = txt.splitlines()

for row in rows:
	name, sex, babies = row.strip().split(',')
	xlist.append([name,sex,babies])

def sort(x):
	return int(x[2])

blist = sorted(xlist, key=sort, reverse=True)
clist = blist[0:10]

num = 0
for baby in clist:
	num +=1
	n = str(num) + "."
	print(n,','.join(str(x) for x in baby))
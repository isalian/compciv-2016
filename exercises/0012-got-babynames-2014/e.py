import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

flist = []
mlist = []

rows = txt.splitlines()

for row in rows:
	name, sex, babies = row.strip().split(',')
	if sex == "F":
		flist.append(babies)
	if sex == "M":
		mlist.append(babies)
flist = [int(i) for i in flist]
mlist = [int(i) for i in mlist]
print("F:", sum(flist))
print("M:", sum(mlist))
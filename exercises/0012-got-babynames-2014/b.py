import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

nlist = []

rows = txt.splitlines()

for row in rows:
	cols = row.split(",")
	nlist.append(cols[2])
nlist = [int(i) for i in nlist]
print("There are", sum(nlist), "babies whose names were recorded in 2014.")
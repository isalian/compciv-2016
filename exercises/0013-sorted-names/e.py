import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

xlist = []

rows = txt.splitlines()

for row in rows:
	name, sex, babies = row.strip().split(',')
	xlist.append(babies)
xlist = [int(i) for i in xlist]
total = sum(xlist)

babydict = {}

for line in rows:
    name, sex, babies = line.strip().split(',')
    if babydict.get(name):
        babydict[name] += int(babies)
    else:
        babydict[name] = int(babies)

nlist = []
for entry in babydict:
	val = babydict[entry]
	nlist.append([entry, val])

def sort(x):
	return int(x[1])

sortlist = sorted(nlist, key=sort, reverse=True)

countlist = []

for baby in sortlist:
	countlist.append(int(baby[1]))

set1 = sum(countlist[0:10])
a = (set1/total)*100
print("Names 1 to 10:", round(a, 1))

set2 = sum(countlist[10:100])
b = (set2/total)*100
print("Names 11 to 100:", round(b, 1))

set3 = sum(countlist[100:1000])
c = (set3/total)*100
print("Names 101 to 1000:", round(c, 1))

set4 = sum(countlist[1001:10000])
d = (set4/total)*100
print("Names 1001 to 10000:", round(d, 1))

set5 = sum(countlist[10001:30579])
e = (set5/total)*100
print("Names 10001 to 30579:", round(e, 1))
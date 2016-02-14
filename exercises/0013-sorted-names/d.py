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
	if sex == "F" and "x" in name.lower():
		flist.append([name,babies])
	if sex == "M" and "x" in name.lower():
		mlist.append([name,babies])

def sort(x):
	return int(x[1])

sortf = sorted(flist, key=sort, reverse=True)
sortm = sorted(mlist, key=sort, reverse=True)

print("Female")
fnum = 0
for baby in sortf[0:5]:
	fnum +=1
	n = str(fnum) + "."
	print(n, baby[0].ljust(11), str(baby[1]).rjust(6))

print("Male")
mnum = 0
for baby in sortm[0:5]:
	mnum +=1
	n = str(mnum) + "."
	print(n, baby[0].ljust(11), str(baby[1].rjust(6)))
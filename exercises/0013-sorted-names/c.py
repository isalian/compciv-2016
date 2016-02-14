import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

babydict = {}
rows = txt.splitlines()

for line in rows:
    name, sex, babies = line.strip().split(',')
    if babydict.get(name):
        babydict[name] += int(babies)
    else:
        babydict[name] = int(babies)

poplist = []
for entry in babydict:
	val = babydict[entry]
	if val > 1999:
		poplist.append([entry, val])
		
def sort(x):
	return(len(x[0]), int(x[1]))

sortlist = sorted(poplist, key=sort, reverse=True)

for baby in sortlist[0:10]:
	print(baby[0].ljust(11), str(baby[1]).rjust(10))
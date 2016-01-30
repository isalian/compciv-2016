import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()

rows = txt.splitlines()
line_num = 0

print("Top baby girl names")
for line in rows[0:5]:
	name, sex, babies = line.strip().split(',')
	line_num += 1
	l = str(line_num) + "."
	print(l, name, babies)

print("\n")
print("Top baby boy names")

nlist = []
for line in rows:
	name, sex, babies = line.strip().split(',')
	if sex == "M":
		nlist.append([name,babies])
blist = nlist[0:5]
bnum = 0
for line in blist:
	bnum +=1
	n = str(bnum) + "."
	print(n, line[0], line[1])
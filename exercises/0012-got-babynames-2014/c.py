import os
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

rows = txt.splitlines()

nlist = []
for row in rows:
	name, sex, babies = row.strip().split(',')
	if name == 'Daenerys':
		print("Daenerys:", babies)
	if "Khalees" in name:
		nlist.append(babies)
	if "Khaless" in name:
		nlist.append(babies)
nlist = [int(i) for i in nlist]
print("Khaleesi:", sum(nlist))


import os
import string
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

rows = txt.splitlines()

mydict = {}
for line in rows:
	name, sex, babies = line.strip().split(',')
	endletter = name[-1]
	if mydict.get(endletter):
		mydict[endletter] += int(babies)
	else:
		mydict[endletter] = int(babies)
for letter in string.ascii_lowercase:
	val = mydict[letter]
	l = str(letter) + ":"
	print(l, val)
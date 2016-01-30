import os
import string
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
f = open (zname ,'r')
txt = f.read ()
f.close ()

rows = txt.splitlines()

mydict = {'M': {}, 'F': {}}
fdict = mydict['F']
mdict = mydict['M']
for line in rows:
	name, sex, babies = line.strip().split(',')
	endletter = name[-1]
	if sex == 'F':
		if fdict.get(endletter):
			fdict[endletter] += int(babies)
		else:
			fdict[endletter] = int(babies)
	if sex == 'M':
		if mdict.get(endletter):
			mdict[endletter] += int(babies)
		else:
			mdict[endletter] = int(babies)
print("letter", 'F'.rjust(5), 'M'.rjust(7))
print ("--------------------")
for letter in string.ascii_lowercase:
	fval = str(fdict[letter])
	mval = str(mdict[letter])
	print(letter, fval.rjust(10), mval.rjust(7))
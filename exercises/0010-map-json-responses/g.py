import os
import json
zname = os.path.join('tempdata', 'mapzen', "stanford.json")
f = open (zname ,'r')
txt = f.read ()
f.close ()

mydict = json.loads(txt)
data = mydict['features']
for xdict in data:
	z = xdict['properties']
	mylist = []
	mylist.append(z['label'])
	mylist.append(z['confidence'])
	geo = xdict['geometry']
	xy = geo['coordinates']
	mylist.extend(xy)
	print(";".join([str(x) for x in mylist]))
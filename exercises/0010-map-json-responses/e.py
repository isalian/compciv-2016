import os
import json
zname = os.path.join('tempdata', 'googlemaps', "stanford.json")
f = open (zname ,'r')
txt = f.read ()
f.close ()

mydict = json.loads(txt)

zlist = []
for x in mydict['results']:
	zlist.append(x['formatted_address'])

meh = mydict['results']
geo = meh.pop(0)
loc = geo['geometry']
x = loc['location']

zlist.append(x['lng'])
zlist.append(x['lat'])

print(";".join([str(x) for x in zlist]))
import os
import json
zname = os.path.join('tempdata', 'googlemaps', "stanford.json")
f = open (zname ,'r')
txt = f.read ()
f.close ()

mydict = json.loads(txt)

for x in mydict['results']:
	print(x['formatted_address'])

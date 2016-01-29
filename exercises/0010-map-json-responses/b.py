import os
import json
zname = os.path.join('tempdata', 'googlemaps', "stanford.json")
f = open (zname ,'r')
txt = f.read ()
f.close ()

mydict = json.loads(txt)

print(mydict['status'])
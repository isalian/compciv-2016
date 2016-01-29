import os
import json
zname = os.path.join('tempdata', 'mapzen', "stanford.json")
f = open (zname ,'r')
txt = f.read ()
f.close ()

mydict = json.loads(txt)

print("type:", mydict['type'])

blah = mydict['geocoding']
info = blah['query']
print("text:", info['text'])
print("size:", info['size'])
print("boundary.country:", info['boundary.country'])
import os
import json
import requests
os.makedirs("tempdata", exist_ok = True) 

zipurl = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson'
resp = requests.get(zipurl)
zname = os.path.join('tempdata', "earthquakes-4.5_month.txt")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()

f = open(zname, 'r')
txt = f.read ()
f.close ()

mydict = json.loads(txt)

print(len(mydict['features']))
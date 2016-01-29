import os
import requests
print("---")
os.makedirs("tempdata/googlemaps", exist_ok = True) 
zipurl = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
resp = requests.get(zipurl)
print ("Downloading from:", zipurl)

zname = os.path.join('tempdata', 'googlemaps', "stanford.json")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()
print ("Writing to:", zname)
zfile = open(zname,'r')
mylist = list(str.splitlines(resp.text))
zfile.close()
print("Wrote", len(mylist), "lines and", len(resp.content), "characters")

print("---")
os.makedirs("tempdata/mapzen", exist_ok = True)
zipurl = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
resp = requests.get(zipurl)
print ("Downloading from:", zipurl)

zname = os.path.join('tempdata', 'mapzen', "stanford.json")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()
print ("Writing to:", zname)
zfile = open(zname,'r')
mylist = list(str.splitlines(resp.text))
zfile.close()
print("Wrote", len(mylist), "lines and", len(resp.content), "characters")
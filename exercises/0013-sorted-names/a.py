import os
import requests
os.makedirs("tempdata", exist_ok = True) 

zipurl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(zipurl)
zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()

print("There are", len(resp.content), "characters in", zname)
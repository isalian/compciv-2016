import requests
import os
zipurl = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
resp = requests.get(zipurl)
print ("Downloading:", zipurl)

zname = os.path.join('tempdata', "matty.shakespeare.tar.gz")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()
print ("Writing file:", zname)

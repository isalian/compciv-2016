import requests
import os

source = "http://www.fjc.gov/history/export/jb.txt"
datadirectory = 'tempdata'
data = os.path.join(datadirectory, 'judges.csv')
os.makedirs(datadirectory, exist_ok=True)

print("Downloading", source)
resp = requests.get(source)

with open(data, 'wb') as x:
	x.write(resp.content)
	x.close

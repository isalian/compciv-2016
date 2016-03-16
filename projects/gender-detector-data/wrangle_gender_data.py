from os.path import join, basename
import csv
import json
DATA_DIR = 'tempdata'
wrangleheaders = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
csvwrangle = join(DATA_DIR, 'wrangledbabynames.csv')

firstyear = 1950
lastyear = 2014
years = list(range(firstyear, lastyear, 10))
years.append(lastyear)

namesdict = {}
for year in years:
	filename = join(DATA_DIR, 'yob' + str(year) + '.txt')
	print("Parsing", filename)
	thefile = open(filename, 'r')

	for line in thefile:
		name, gender, count = line.split(',')
		if not namesdict.get(name):
			namesdict[name] = {'M': 0, 'F':0}
		namesdict[name][gender] += int(count)

biglist = []

for name, babiescount in namesdict.items():
	xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
	xdict['total'] = xdict['females'] + xdict['males']
	if xdict['females'] >= xdict['males']:
		xdict['gender'] = 'F'
		xdict['ratio'] = round(100 * (xdict['females']/xdict['total']))
	else:
		xdict['gender'] = 'M'
		xdict['ratio'] = round(100 * (xdict['males']/xdict['total']))
	biglist.append(xdict)

wfile = open(csvwrangle, 'w')
wcsv = csv.DictWriter(wfile, fieldnames = wrangleheaders)
wcsv.writeheader()

def func(xdict):
	return(-xdict['total'], xdict['name'])

finallist = sorted(biglist, key = func)
for row in finallist:
	wcsv.writerow(row)
wfile.close()

jsonwrangle = join(DATA_DIR, 'wrangledbabynames.json')

with open(csvwrangle, 'r') as rfile:
    datarows = list(csv.DictReader(rfile))

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

whateverfile = open(jsonwrangle, 'w')
jsontext = json.dumps(datarows, indent=2)
whateverfile.write(jsontext)
whateverfile.close()

from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
wrangleheaders = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
wranglefilename = join(DATA_DIR, 'wrangledbabynames.csv')

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

wfile = open(wranglefilename, 'w')
wcsv = csv.DictWriter(wfile, fieldnames = wrangleheaders)
wcsv.writeheader()

def func(xdict):
	return(-xdict['total'], xdict['name'])

finallist = sorted(biglist, key = func)
for row in finallist:
	wcsv.writerow(row)
wfile.close()

theend = open(wranglefilename, 'r')
firstlines = theend.readlines()[0:10]
for line in firstlines:
	print(line.strip())
from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
yr = 2014
filename = join(DATA_DIR, 'yob' + str(yr) + '.txt')
wrangleheaders = ['year', 'name', 'gender', 'ratio', 'females', 'males', 'total']
wranglefilename = join(DATA_DIR, 'wrangled2014.csv')

names_dict = {}
thefile = open(filename, 'r')

for line in thefile:
    name, gender, count = line.split(',')
    if not names_dict.get(name):
        names_dict[name] = {'M': 0, 'F':0}
    names_dict[name][gender] += int(count)

biglist = []

for name, counts in names_dict.items():
	xdict = {}
	xdict['year'] = yr
	xdict['name'] = name
	xdict['females'] = counts['F']
	xdict['males'] = counts['M']
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
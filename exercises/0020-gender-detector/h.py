from os.path import join
import csv
DATA_DIR = 'tempdata'
wranglefilename = join(DATA_DIR, 'wrangled2014.csv')

thefile = open(wranglefilename, 'r')
data = list(csv.DictReader(thefile))

for r in data:
	r['total'] = int(r['total'])
	r['males'] = int(r['males'])
	r['females'] = int(r['females'])
	r['ratio'] = int(r['ratio'])

print("Most popular names with <= 60% gender skew:")
sortrows = sorted(data,key=lambda r: r['total'], reverse=True)

fxrows = [r for r in sortrows if r['ratio'] <= 60]
for row in fxrows[0:5]:
	print(row['name'].ljust(10), row['gender'], row['ratio'], row['total'])
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

bigdatarows = []
for row in data:
    if row['total'] >= 100:
          bigdatarows.append(row)

popular = len(bigdatarows)

print("Popular names with a gender ratio bias of less than or equal to:")
for genderratio in (60, 70, 80, 90, 99):
	finallist = [r for r in bigdatarows if r['ratio'] <= genderratio]
	print(str(genderratio) + '%: ', str(len(finallist)) + '/' + str(popular))
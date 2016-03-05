from os.path import join
import csv
DATA_DIR = 'tempdata'
wranglefinal = join(DATA_DIR, 'wrangledbabynames.csv')

namesrows = list(csv.DictReader(open(wranglefinal)))

for r in namesrows:
	r['total'] = int(r['total'])
	r['males'] = int(r['males'])
	r['females'] = int(r['females'])
	r['ratio'] = int(r['ratio'])

def genderdetector(name):
	result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
	for row in namesrows:
		if name.lower() == row['name'].lower():
			result = row
			break
	return result

testing = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']

namecount = {'M': 0, 'F': 0, 'NA': 0}
babycount = {'males': 0, 'females': 0}
for name in testing:
	result = genderdetector(name)
	print(name, result['gender'], result['ratio'])
	if result['gender']:
		namecount[result['gender']] += 1
	if result['gender'] != 'NA':  # we don't want to count the NA's
		babycount['males'] += result['males']
		babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])    
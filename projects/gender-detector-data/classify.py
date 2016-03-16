import os
import csv
from gender import detect_gender

datadirectory = 'tempdata'
wranglefilename = os.path.join(datadirectory, 'wrangled_data.csv')
classifyfilename = os.path.join(datadirectory, 'classified_data.csv')
classifyheaders = ['firstname', 'lastname', 'birthyear', 'gender', 'race', 'party', 'usable_name', 'detected_gender', 'ratio']


def extract_usable_name(namestr):
	nameparts = namestr.split(' ')
	for n in nameparts:
		if '[' not in n:
			if '.' not in n:
				return n
	return ""		

f = open(classifyfilename, 'w', newline='')
fwrite = csv.DictWriter(f, fieldnames=classifyheaders)
fwrite.writeheader()

with open(wranglefilename) as r:
	datarows = list(csv.DictReader(r))
	ct = 0
	for row in datarows:
		usablename = extract_usable_name(row['firstname'])
		ct += 1
		print("Row:", ct, "extracting --", usablename, "-- from:", row['firstname'])
		genderresults = detect_gender(usablename)
		row['usable_name'] = usablename
		row ['detected_gender'] = genderresults['gender']
		row['ratio'] = genderresults['ratio']
		fwrite.writerow(row)

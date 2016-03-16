from os.path import join
from csv import DictReader

datadirectory = 'tempdata'
cfile = join(datadirectory, 'classified_data.csv')

with open(cfile) as r:
	rows = list(DictReader(r))

###Tells you gender totals and ratio of female to male judges
	print("-----------------") 
	print("Total gender ratio for judges:")
	stats = {'M': 0, 'F': 0, 'NA': 0}
	for row in rows:
		gdata = row['detected_gender']
		stats[gdata] += 1
	print("F:", stats['F'], "M:", stats['M'], "NA:",stats['NA'])
	femdata = round((stats['F']/stats['M']) * 100)
	print(str(femdata) + '%', 'of federal judges since 1789 have been female')

###Tells you how many people are both female and minorities versus male and minorities
	print("-----------------") 
	print("Minority judges by gender:")
	fminorities = []
	mminorities = []
	for row in rows:
		if row['race'] != 'White':
			if row['detected_gender']== 'F':
				fminorities.append(row['firstname'])
			if row['detected_gender'] == 'M':
				mminorities.append(row['firstname'])
	totalz = len(fminorities) + len(mminorities)
	femz = round((len(fminorities)/totalz) * 100)
	femi = round((len(fminorities)/len(rows)) * 100)
	print("F:", len(fminorities), "M:", len(mminorities))
	print("Total non-White judges since 1789:", totalz, "out of", (stats['F'] + stats['M'] + stats['NA']))
	print(str(femi) + '%', 'of federal judges since 1789 have been female minorities')
	print(str(femz) + '%', 'of federal MINORITY judges since 1789 have also been female')

###Tells you how many females, minorities appointed by Democrat v. Republican presidents
	print("-----------------") 
	print("Gender ratio for judges by president's political party:")
	totald = []
	totalr = []
	dwomen = []
	rwomen = []
	for row in rows:
		if row['party'] == 'Democratic':
			totald.append(row['firstname'])
			if row['detected_gender']== 'F':
				dwomen.append(row['firstname'])
		else:
			totalr.append(row['firstname'])
			if row['detected_gender'] == 'F':
				rwomen.append(row['firstname'])
	dratio = round((len(dwomen)/len(totald)) * 100)
	rratio = round((len(rwomen)/len(totalr)) * 100)
	print(str(dratio) + '%', 'of Democratic judicial appointees since 1789 have been female')
	print(str(rratio) + '%', 'of Republican judicial appointees since 1789 have been female')

###Tells you how accurate the gender detector program is by comparing gender to detected_gender
	print("-----------------") 
	print("Accuracy of this program:")
	errors = []
	for row in rows:
		if row['gender'] != row['detected_gender']:
			errors.append(row['firstname'])
	print('There were', len(errors), 'total incorrect gender readings by this program')
	print('This program was', (str(100 - round((len(errors)/len(rows))*100))) + '%', "accurate at detecting a judge's gender")
import os
import csv
datadirectory = 'tempdata'
data = os.path.join(datadirectory, 'judges.csv')
wrangleheaders = ['firstname', 'lastname', 'birthyear', 'gender', 'race', 'party']
wranglefilename = os.path.join(datadirectory, 'wrangled_data.csv')
swaglist = []

with open(data) as csvfile:
	rdr = csv.DictReader(csvfile)
	for row in rdr:

		xdict = {}
		xdict['firstname'] = row['Judge First Name']
		xdict['lastname'] = row['Judge Last Name']
		xdict['birthyear'] = row['Birth year'] 
		xdict['gender'] = row['Gender']
		xdict['race'] = row['Race or Ethnicity']
		xdict['party'] = row['Party Affiliation of President']

		swaglist.append(xdict)

wfile = open(wranglefilename, 'w', newline='')
writer = csv.DictWriter(wfile, fieldnames=wrangleheaders)
writer.writeheader()
print("Writing to", wranglefilename)
for row in swaglist:
	writer.writerow(row)
wfile.close()
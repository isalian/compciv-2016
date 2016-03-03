from os.path import join, basename

yr = 2014
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'yob' + str(yr) + '.txt')

names_dict = {}
thefile = open(filename, 'r')

for line in thefile:
	name, gender, count = line.split(',')
	if not names_dict.get(name):
		names_dict[name] = {'M': 0, 'F':0}
	names_dict[name][gender] += int(count)

thefile.close()

totalnames = len(names_dict.keys())

totalbabies = 0 
for b in names_dict.values():
	total = b['M'] + b['F']
	totalbabies += total 
print("Total:", totalnames, 'unique names for', totalbabies, 'babies')

for gender in ['M', 'F']:
    ncount = 0
    bcount = 0
    for v in names_dict.values():
        if v[gender] > 0:
            bcount += v[gender]
            ncount += 1
    print("    %s:" % gender, ncount, "unique names for", bcount, "babies")
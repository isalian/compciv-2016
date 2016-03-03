from os.path import join, basename

DATA_DIR = 'tempdata'
START_YEAR = 1950
END_YEAR = 2015

for year in range(START_YEAR, END_YEAR, 5):
    print(year)
    filename = join(DATA_DIR, 'yob' + str(year) + '.txt')

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
    print("Total:", round(totalbabies/totalnames), 'babies per name')

    for gender in ['M', 'F']:
        ncount = 0
        bcount = 0
        for v in names_dict.values():
            if v[gender] > 0:
                bcount += v[gender]
                ncount += 1
        print("    %s:" % gender, round(bcount/ncount), "babies per name")
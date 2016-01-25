import os
fname = os.path.join("tempdata", "tragedies", "hamlet")
f = open(fname, 'r')
for x in range(5):
    print(f.readline().strip())
f.close()
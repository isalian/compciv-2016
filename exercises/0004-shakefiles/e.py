import os
fname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile = open(fname, 'r')
line_num = 0
for x in hamletfile:
	line_num += 1
hamletfile.close()
print(fname, "has", line_num, "lines")
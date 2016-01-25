from glob import glob
from os.path import join
tragic_path = join('tempdata', 'tragedies', '*')
tragic_filenames = glob(tragic_path)

for fname in tragic_filenames:
	txtfile = open(fname, 'r')
	total_lines = 0
	for line in txtfile:
		total_lines += 1
	txtfile.close()
	print(fname, "has", total_lines, "lines")
	starting_line_num = total_lines - 5
	txtfile = open(fname, 'r')
	for line_num in range (total_lines): 
		line = txtfile.readline()
		if line_num >= starting_line_num:
			the_line = str(line_num + 1) + ": " + line.strip()
			print(the_line)
txtfile.close()
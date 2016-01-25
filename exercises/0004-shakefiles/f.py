import os
fname = os.path.join("tempdata", "tragedies", "romeoandjuliet")
total_lines = 4766
starting_line_num = total_lines - 5

txtfile = open(fname, 'r')
for line_num in range(total_lines):
	line = txtfile.readline()
	if line_num >= starting_line_num:
		the_line = str(line_num + 1) + ": " + line.strip()
		print(the_line)
txtfile.close()
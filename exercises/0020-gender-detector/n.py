from zoofoo import detect_gender

names = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']
namecount = {'M': 0, 'F': 0, 'NA': 0}
babycount = {'males': 0, 'females': 0}
for name in names:
	result = detect_gender(name)
	print(name, result['gender'], result['ratio'])
	if result['gender']:
		namecount[result['gender']] += 1
	if result['gender'] != 'NA':  
		babycount['males'] += result['males']
		babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])    
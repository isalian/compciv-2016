from os.path import join
import json
import csv
DATA_DIR = 'tempdata'
csvwrangle = join(DATA_DIR, 'wrangledbabynames.csv')
jsonwrangle = join(DATA_DIR, 'wrangledbabynames.json')

with open(csvwrangle, 'r') as rfile:
    datarows = list(csv.DictReader(rfile))

for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])

whateverfile = open(jsonwrangle, 'w')
jsontext = json.dumps(datarows, indent=2)
whateverfile.write(jsontext)
whateverfile.close()

csvtxt = open(csvwrangle).read()
jsontxt = open(jsonwrangle).read()

print("CSV has", len(csvtxt), "characters")
print("JSON has", len(jsontxt), "characters")

ratio = round(((len(jsontxt) - len(csvtxt)) / len(csvtxt)), 1)
print("JSON requires", ratio, "times more text characters than CSV")
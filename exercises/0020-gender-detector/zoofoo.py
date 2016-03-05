from os.path import join
import json
DATA_DIR = 'tempdata'
jsonwrangle = join(DATA_DIR, 'wrangledbabynames.json')
namesrows = json.load(open(jsonwrangle))

def detect_gender(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': 0, 'females': 0, 'total': 0 }
    for row in namesrows:
        if name.lower() == row['name'].lower():
            result = row
            break
    return result
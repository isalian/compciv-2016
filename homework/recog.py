import requests
from os.path import join, basename
from os import makedirs
from glob import glob
import json
api = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify'
PICS_DIR = 'pics'
RECOG_DIR = 'responses'
makedirs(RECOG_DIR, exist_ok=True)
mycreds = 'creds_watson_visual.json'

params = {
    'version': '2015-12-02'
}
headers = {
    'Accept': 'application/json'
}

creds = json.load(open(mycreds))
my_username = creds['credentials']['username']
my_password = creds['credentials']['password']
myauth = (my_username, my_password)

for fname in glob(join(PICS_DIR, '*.jpg')):
    print("Testing", fname)
    with open(fname, 'rb') as imgdata:
         mydict = {}
         mydict['images_file'] = (basename(fname), imgdata)
         resp = requests.post(api, params=params,
                       auth=myauth, headers=headers,
                       files=mydict)
         print(resp.status_code)
    if resp.status_code == 200:
        oname = join(RECOG_DIR, basename(fname + '.json'))
        print("Writing to:", oname)

        with open(oname, 'w') as o:
            o.write(resp.text)

    else:
        print("Error code was", resp.status_code, " -- not: 200")
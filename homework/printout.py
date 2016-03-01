from os.path import join, basename
from glob import glob
import json
PICS_DIR = 'pics'
RECOG_DIR = 'responses'


HTML_FILENAME = 'printout.html'
htmlfile = open(HTML_FILENAME, 'w')
htmlfile.write("<html><title>Hello</title><body>")
htmlfile.write("<h1>My name is Isha and this is my IBM Watson image analysis</h1>")

for jsonname in glob(join(RECOG_DIR, '*.json')):
    print("Extracting", jsonname)
    j = json.load(open(jsonname))
    img = j['images'][0]
    imgname = img['image']
    htmlfile.write("<h2>%s</h2>" % imgname)


    imgfilename = join(PICS_DIR, imgname)
    htmlfile.write('<img src="%s">' % imgfilename)

    bnum = 0
    scores = img['scores']
    for entry in scores:
        olist = []
        bnum +=1
        n = str(bnum) + ". "
        line = n + entry['classifier_id'] + " -- " + str(entry['score'])
        htmlfile.write("<ol>%s</ol>" % line)

htmlfile.close()
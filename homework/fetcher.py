import os
import requests
import string

os.makedirs("pics", exist_ok = True)

urldict = {'a': 'https://upload.wikimedia.org/wikipedia/commons/9/95/Breads_with_green_dipping_sauce.jpg',
 'b' : 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Flickr_-_cyclonebill_-_Kartoffelpizza_med_rosmarinpesto.jpg',
 'c' : 'https://upload.wikimedia.org/wikipedia/commons/8/84/Finished_nettle_ravioli_%285732552463%29.jpg',
 'd' : 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Food_2010-by-RaBoe-060.jpg',
 'e' : 'https://upload.wikimedia.org/wikipedia/commons/8/8c/Tartufo.jpg'}

for key in urldict.keys():
	val = urldict[key]
	print("Downloading", val)
	resp = requests.get(val)
	zname = os.path.join('pics', key + ".jpg")
	print("Saving to", zname)
	zfile = open(zname, 'wb')
	zfile.write(resp.content)
	zfile.close()
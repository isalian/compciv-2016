import requests
url = "https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
resp = requests.get(url)
a = resp.text
print (a.count('Applause'))
print (a.lower().count("applause"))
print (a.count("<p>"))
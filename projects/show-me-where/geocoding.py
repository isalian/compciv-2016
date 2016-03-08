import requests
import json


def read_mapzen_credentials():
	creds_filename = 'creds_mapzen.txt'
	keytext = open(creds_filename).read().strip()
	return keytext

def fetch_mapzen_response(location):
	"""
	'location is a text string you send to Mapzen's API to geocode
	This function returns a JSON-formatted text string from the Mapzen API
	"""
	mykey = read_mapzen_credentials()
	my_params = {'text': location, 'api_key': mykey}
	resp = requests.get("https://search.mapzen.com/v1/search", params = my_params)
	return resp.text

def parse_mapzen_response(txt):
	"""
	`txt` is a string containing JSON-formatted text from Mapzen's API

	returns a dictionary containing the useful key/values from the most relevant result
	"""
	gdict = {} 
    data = json.loads(txt)
    if data['features']: 
        gdict['status'] = 'OK'
        feature = data['features'][0]  
        props = feature['properties']  
        gdict['confidence'] = props['confidence']
        gdict['label'] = props['label']
        
        coords = feature['geometry']['coordinates']
        gdict['longitude'] = coords[0]
        gdict['latitude'] = coords[1]
    else:
        gdict['status'] = None
    return gdict

def geocode(location):
    """
    Geocode a location string using the Mapzen Search API

    What it expects:
    ----------------
    It expects `location` is a string which corresponds to some kind of human-readable geographical location, e.g. "Stanford, CA"

    It also expects the variable `CREDS_FILE` to corespond to an existing file
    that contains a valid Mapzen Search key.

    What it does:
    -------------
    It opens and reads the file at CREDS_FILE to get the API key.

    It calls the Mapzen Search API with an HTTP request, using the API key, 
    and user-provided `location` string as the `text` parameter.

    It translates the Mapzen Search response into a dictionary, using
    the JSON library.

    It creates a dictionary.

    What it returns:
    ----------------
    A dictionary containing these key-value pairs:

    - query_text: the `location` string provided by the user
    - label: The string label that Mapzen provides in describing the found location
    - confidence: A float representing the confidence value that Mapzen has in its result.
    - latitude: a float representing the latitude coordinate
    - longitude: a float representing the longitude coordinate
    - status: "OK", a string that indicates a result was found. Else, None
    """
    rawtext = fetch_mapzen_response(location)
    mydict = parse_mapzen_response(rawtext)
    mydict['query_string'] = location
    return mydict
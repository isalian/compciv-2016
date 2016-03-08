from utils.geocoding import geocode

B_X = "\033[1m"
B_Z = "\033[0m"

intro = input("What do you want to do? ")
if intro == "hello":
	usertext = input("What is your name? ")
	print("Hello", B_X + usertext + B_Z)
elif intro == 'geocode':
	location = input("What is your location? ")
	print("Ok...geocoding:", location)
	georesult = geocode(location)
	print(georesult)
elif intro == 'help':
	print(geocode.__name__)   
	print(geocode.__doc__)
else:
	print("Sorry, I don't know how to respond to", intro)

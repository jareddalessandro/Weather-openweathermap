#Uses openweathermap's API to give weather information.
import json
import urllib.request
import os

#The url without api key and with units set to imperial. Put your APIKEY from openweathermap.org where shown below
#Using string concatenation to make user input for location possible
first_url = "http://api.openweathermap.org/data/2.5/weather?q="
second_url = "&APPID=APIKEY&units=imperial"
location = ""
while True:
	location = input("Enter city name: ")
	if len(location) < 1:
		print("\n","==== No Name Entered ====", "\n")
		continue
	else:
		url = first_url + location + second_url
		os.system("cls")
		break

while True:
	#Opening url and getting back byte data.
	#Use decode(utf-8) to make the bytes usable, str() would not turn the bytes into str
	try:
	    print("Retrieving...")
	    uh = urllib.request.urlopen(url)
	    data = uh.read()
	    js = json.loads(data.decode("utf-8"))
	    print("Retrieval successful")
	except:
		print("==== Failure to Retrieve ====")
		usr=input()

	#Get the desired information into variables.
	#If JSON has an extra bracket you will need [0] to get to the inner stuff.
	#print(json.dumps(js, indent = 4))
	current_temp = js["main"]["temp"]
	wind_speed = js["wind"]["speed"]
	humidity = js["main"]["humidity"]
	description = js["weather"][0]["description"]
	pressure = js["main"]["pressure"]

	#Round variables. Gets rid of decimals
	current_temp = round(current_temp)
	wind_speed = round(wind_speed)

	#print the stuff
	print("Showing Weather for:", location, "\n")
	print("Current atmospheric description:", description)
	print("Current Temperature:", current_temp, "fahrenheit")
	print("Humidity:", humidity, "%")
	print("Wind speed:", wind_speed, "mph")
	print("Atmospheric Pressure:", pressure, "hPa")
	print("")

	#For refreshing, and cleaning screen
	refresh = input("To refresh press ENTER\n")
	if len(refresh) < 1:
		os.system("cls")
		continue
	else:
		break

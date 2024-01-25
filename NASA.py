# Importerer de nødvendige modulene
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
# Åpner URLen
response = urllib.request.urlopen(url)

# laster og leser JSON filen
result = json.loads(response.read())

# Åpner tekst filen når du runer koden
file = open("iss.txt", "w")
file.write("There are currently " +
           str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# Printer ut longitude og latitude i terminalen
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setter opp verden kartet i en turtle modul
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Laster opp verdenskartet
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # Oppdaterer informasjonen til romstasjonen i sanntid
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Henter ut Lan og Lon
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Printer ut Lan og Lon
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Oppdaterer stillngen på kartet
    iss.goto(lon, lat)

    # Oppdaterer hvert 5 sekund
    time.sleep(5)
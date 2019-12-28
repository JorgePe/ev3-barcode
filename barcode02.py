#! /usr/bin/env python3

# if you are running from ssh session invoke this script with 'brickrun'

from ev3dev2 .sound import Sound
import urllib.request
import json

sound = Sound()

#you can get a free trial API key at "https://www.barcodelookup.com/api"
api_key = ""

while True:
    sound.beep()
    ucc = input('Scan a UCC: ')
    ucc = ucc.lower().strip().replace('\t','').replace('\n','')

    url = "https://api.barcodelookup.com/v2/products?barcode=" + ucc + "&formatted=y&key=" + api_key

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    barcode = data["products"][0]["barcode_number"]

    name = data["products"][0]["product_name"]
    brand = data["products"][0]["brand"]
    mpn = data["products"][0]["mpn"]
    description = data["products"][0]["description"]

    sound.speak("Brand:")
    sound.speak(brand)
    
    sound.speak("Model:")
    sound.speak(mpn)
    
    sound.speak("Name:")
    sound.speak(name)

    sound.speak(description)

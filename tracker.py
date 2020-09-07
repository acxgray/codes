# Author: acxgray <nedmostoles@gmail.com>
# A simple python program to track latest COVID 19 Cases at the Philippines
# using Apify API

import requests
import json
from datetime import datetime

response = requests.get("https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true")

# Print API Response Code
# print(response.json())

# function to print data from API as json
# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(response.json())

data = json.loads(response.text)
date = datetime.now()

print("COVID-19 Tracker")
print("As of: " + str(date.strftime("%b %d %Y %H:%M:%S %Z")))
print("Country: " + data['country'])
print("Active Cases: " + str(data['activeCases']))
print("Infected: " + str(data['infected']))
print("Recovered: " + str(data['recovered']))
print("Deceased: " + str(data['deceased']))

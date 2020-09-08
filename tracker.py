# Author: acxgray <nedmostoles@gmail.com>
# A simple python program to track latest COVID 19 Cases at the Philippines
# using Apify API

# API Source
# https://github.com/javieraviles/covidAPI

import requests
import json
import sys
import os
from datetime import datetime


class Tracker:
    def __init__(self, country):
        self.country = country

def menu():
    prog = True
    while prog == True:
        try:
            os.system('cls')
            print("COVID 19 Tracker")
            print("1. Philippines")
            print("2. Japan")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print()
                t = Tracker("philippines")
                response = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + t.country)
                data = json.loads(response.text)
                date = datetime.now()
                print("As of: " + str(date.strftime("%b %d %Y %H:%M:%S %Z")))
                print("Country: " + data['country'])
                print("Active Cases: " + str(data['active']))
                print("Total Cases: " + str(data['cases']))
                print("Recovered: " + str(data['recovered']))
                print("Deceased: " + str(data['deaths']))
                print()
                choice = input("Press ENTER to continue")
            elif choice == 2:
                print()
                t = Tracker("japan")
                response = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + t.country)
                data = json.loads(response.text)
                date = datetime.now()
                print("As of: " + str(date.strftime("%b %d %Y %H:%M:%S %Z")))
                print("Country: " + data['country'])
                print("Active Cases: " + str(data['active']))
                print("Total Cases: " + str(data['cases']))
                print("Recovered: " + str(data['recovered']))
                print("Deceased: " + str(data['deaths']))
                print()
                choice = input("Press ENTER to continue")
            elif choice == 3:
                prog = False
                exit()
            else:
                print("Invalid Option")
                print()
                choice = input("Press ENTER to continue")
        except ValueError:
            print("Invalid Option")
            print()
            choice = input("Press ENTER to continue")
    
def main():
    menu()

main()

#response = requests.get("https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true")
        

# Print API Response Code
# print(response.json())

# function to print data from API as json
# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(response.json())
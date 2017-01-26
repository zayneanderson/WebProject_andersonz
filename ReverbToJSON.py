import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlReverb = 'https://reverb.com/marketplace/acoustic-guitars'
pageReverb = requests.get(urlReverb)
# Prepare for parsing APNewsBriefs with BeautifulSoup
soupReverb = BeautifulSoup(pageReverb.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for position in soupReverb.find_all('li', class_='card-grid_item'):
    price = position.find('div', class_="product-card__price")
    condition = position.find('div', class_="product-condition__price")
    style = position.find('h4', class_="product-card-body-sized")

    # Make changes to response for APNewsBriefs
    response.append({'price' : price, 'condition' : condition, 'style' : style})
# Write response to JSON file
postingsFile = today + '.Reverb.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()

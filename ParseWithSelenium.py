from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json
import csv

# Create dict for JSON Object
response = []

# Prepare for parsing APNewsBriefs with BeautifulSoup after Scraping with Selenium
browser = webdriver.Chrome()

urlReverb = 'https://reverb.com/marketplace/acoustic-guitars'
pageReverb = browser.get(urlReverb)
soupReverb = BeautifulSoup(browser.page_source, 'lxml')

browser.quit()

# Parse APNewsBriefs urlbrowser.page_source
today = str(datetime.datetime.now().date())

for position in soupReverb.find_all('li', class_='card-grid_item'):
        price = position.find('div', class_="product-card__price")
        condition = position.find('div', class_="product-condition__price")
        style = position.find('h4', class_="product-card-body-sized")

    # Make changes to response for APNewsBriefs
        response.append({'price': price, 'condition': condition, 'style': style})

# Write response to JSON file
postingsFile = today + '.Reverb.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()

# Write response to CSV file
keys = response[0].keys()
with open(today + '.Revern.APNewsBriefs.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(response)
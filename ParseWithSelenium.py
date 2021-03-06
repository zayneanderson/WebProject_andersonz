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

#sweetwater
browser.quit()

# Parse APNewsBriefs urlbrowser.page_source
today = str(datetime.datetime.now().date())

#for position in soupReverb.find('li', class_='card-grid_item'):
position =soupReverb.find('li', class_='card-grid__item')
price = position.find('div', class_="product-card__price").span.string
condition = position.find('span', class_="condition-bar__label").string
style = position.find('h4', class_="product-card-body-sized").string
response.append({'price': price, 'condition': condition, 'style': style})

# Write response to JSON file
postingsFile = '/Users/Zayne/Desktop/CSC3130/WebProject_andersonz' + today + '.Reverb.json'
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()

# Write response to CSV file
#keys = response[0].keys()
#with open(today + 'Reverb.csv', 'w') as output_file:
  #  dict_writer = csv.DictWriter(output_file, keys)
    #dict_writer.writeheader()
  #  dict_writer.writerows(response)
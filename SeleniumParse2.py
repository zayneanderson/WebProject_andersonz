from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json

# Create dict for JSON Object
response = []

# Prepare for parsing APNewsBriefs with BeautifulSoup after Scraping with Selenium
browser = webdriver.Chrome()

urlSweetwater = 'https://www.sweetwater.com/c600--6_string_Acoustic_Guitars'
pageSweetwater = browser.get(urlSweetwater)
soupSweetwater = BeautifulSoup(browser.page_source, 'lxml')

browser.quit()

# Parse APNewsBriefs urlbrowser.page_source
today = str(datetime.datetime.now().date())
for position in soupSweetwater.find_all('div', class_='product__info'):
    name = position.find('h2', class_='product__name').string
    description = position.find('span', class_="product__description").string
    price = position.find('div', class_='product__finalrow').next_element.next_element.next_element.next_element.next_element
    print(price)
    #rating = position.find('span', class_='rating__stars')
   # numberOfRatings = position.find('span', class_='rating__count')

    # Make changes to response for APNewsBriefs
    response.append({'name': name, 'description' : description, 'price': price})

# Write response to JSON file
postingsFile = '/Users/Zayne/Desktop/CSC3130/WebProject_andersonz/' + today + '.sweetWater.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
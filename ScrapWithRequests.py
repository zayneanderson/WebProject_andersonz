import requests
import datetime

today = str(datetime.datetime.now()).split(' ')[0]

sites = { 'Reverb-Acoustic Guitars' : 'https://reverb.com/marketplace/acoustic-guitars/'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()
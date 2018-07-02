# Modified version of sample code for extracting href
# tags from URL. see http://www.py4e.com/code3/urllinks.py

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cnt = input('Enter Count - ')
pos = input('Enter Position - ')

num = 0
spos = int(pos)-1

while num <= int(cnt):
    # retrive url file and parse
    print("Retrieving",url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[spos].get('href', None)
    num += 1

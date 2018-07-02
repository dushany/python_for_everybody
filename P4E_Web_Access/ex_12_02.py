# Modified sample code for using python to access web data.
# see http://www.py4e.com/code3/urllink2.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# HTML parses from BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

tot_sum = 0
count = 0

tags = soup('span')
for tag in tags:
    count += 1
    tot_sum += int(tag.contents[0])
print ("Count", count)
print("Sum", tot_sum)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# http://py4e-data.dr-chuck.net/comments_42.xml (sum = 2553)
# http://py4e-data.dr-chuck.net/comments_52861.xml (sum ends with 55)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tot_sum = 0
count = 0

url = input('Enter location: ')
print('Retrieving', url)

# open specified url
data = urllib.request.urlopen(url,context=ctx).read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

for counts in tree.iter('count'):
    count += 1
    tot_sum += int(counts.text)
print('Count:',count)
print('Sum:',tot_sum)

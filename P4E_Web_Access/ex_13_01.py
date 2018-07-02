# program to prompt for a URL, read the JSON data from that URL and
# then parse and extract comment counts from data, and compute sum of numbers

import urllib.request, urllib.parse, urllib.error
import json

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    count = 0
    n_sum = 0

    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    js = json.loads(data)

    for item in js['comments']:
        count += 1
        n_sum += int(item['count'])

    print('Count',count)
    print('Sum',n_sum)

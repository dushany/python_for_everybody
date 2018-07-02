# program to prompt for a URL, read the JSON data from that URL and
# then parse and extract comment counts from data, and compute sum of numbers

import urllib.request, urllib.parse, urllib.error
import json

srv_url = "http://py4e-data.dr-chuck.net/geojson?"

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = srv_url + urllib.parse.urlencode({'address':address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('======= failed to retrieve =======')
        continue

    print('Place ID:',js['results'][0]['place_id'])

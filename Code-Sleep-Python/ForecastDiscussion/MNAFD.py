#!/usr/bin/env python3
import requests

# MPX is the office for Chanhassen National Weather Service Office.
# To find yours, go here: https://www.weather.gov/srh/nwsoffices
myOffice = "mpx"
url = "https://api.weather.gov/products/types/afd/locations/%s" % myOffice

headers = {
    'User-Agent': "Python"
    }

response = requests.request("GET", url, headers=headers)
latestAfd = response.json()['@graph'][0]['@id']
afdJson = requests.request("GET", latestAfd, headers=headers).json()

# These are the two pieces of the JSON that have information we actually want.
print(afdJson['issuanceTime'])
print(afdJson['productText'])

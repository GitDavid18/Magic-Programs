import urllib.request
import json
import requests

baseurl = 'https://api.scryfall.com/cards/named?exact='
# cardname = 'Marchesa-the-black-rose'
cardname = 'marchesa the black rose'

url = (baseurl + cardname).encode()

print('request url: ', url)
response = requests.get(url)
# print(type(response))
# print(response.text)

jcards = response.json()

# print(jcards)
print('------------------')
# for bla in jcards:
    # print(bla)

print('name', jcards['name'])
print('cmc', jcards['cmc'])
print('mana_cost', jcards['mana_cost'])
print('image_uris', jcards['image_uris']['normal'])


# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 
# request = urllib.request.Request(url, None, headers)
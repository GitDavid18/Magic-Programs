import urllib.request
import json
import requests

baseurl = 'https://api.scryfall.com/cards/'

# Search for cardname:
# options = 'named?exact='
# cardname = 'marchesa the black rose'
# url = (baseurl + options + cardname).encode()

options = 'search?order=set&q=t:creature t:legend&dir=desc'
url = (baseurl + options).encode()

# I am just looking through the first page
# add logic for second page
print('request url: ', url)
response = requests.get(url)
# print(type(response))
# print(response.text)
if response.status_code == 200:
    jcards = response.json()
    printedcards = 0
    # print(jcards)
    print('------------------')
    for bla in jcards['data']:
        print(bla.get('name'))
        print('------------------')
        printedcards += 1

    print('I found: ' , jcards['total_cards'],' total cards')
    print('cards printed: ', printedcards)
else:
    print(response)



# print('name', jcards['name'])
# print('cmc', jcards['cmc'])
# print('mana_cost', jcards['mana_cost'])
# print('image_uris', jcards['image_uris']['normal'])


# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
# headers={'User-Agent':user_agent,} 
# request = urllib.request.Request(url, None, headers)
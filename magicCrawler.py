import urllib.request
import json
import requests
import time
import sqlite3

def pullPage(url):
    print('request url: ', url)
    response = requests.get(url)
    # print(type(response))
    # print(response.text)
    if response.status_code == 200:
        jcards = response.json()
        printedcards = 0
        # print(jcards)
        for bla in jcards:
            if bla == 'data': continue
            print(bla, ': ', jcards[bla])
        print('------------------')

        for bla in jcards['data']:
            print(bla.get('name'))
            print('------------------')
            printedcards += 1

        print('I found: ' , jcards['total_cards'],' total cards')
        print('cards printed: ', printedcards)
        
        return jcards.get(('next_page'), None)
        
    else:
        print(response)
        return None


def writeDataToDB(data):
    dbPath = ''
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    
    #write data to database
    
def main(self):

    baseurl = 'https://api.scryfall.com/cards/'

    # Search for cardname:
    # options = 'named?exact='
    # cardname = 'marchesa the black rose'
    # url = (baseurl + options + cardname).encode()

    options = 'search?order=set&q=t:creature t:legend&dir=desc'
    url = (baseurl + options).encode()

    count = 0

    while url is not None:
        
        url = pullPage(url)
        count += 1
        print('current count ', count)
        time.sleep(0.2)
        
if __name__ == "__main__":
    main()
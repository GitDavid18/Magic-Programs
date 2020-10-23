import urllib.request
import json
import requests
import time
import sqlite3

dbPath = 'D:\\Dokumente\\Programming\\Magic programs\\MTGLegends.sqlite'
conn = sqlite3.connect(dbPath)
cur = conn.cursor()

def pullPage(url):
    print('request url: ', url)
    response = requests.get(url)
    # print(type(response))
    # print(response.text)
    if response.status_code == 200:
        jcards = response.json()
        printedcards = 0
        # print(jcards)
        for card in jcards:
            if card == 'data': continue
            print(card, ': ', jcards[card])
        print('------------------')

        for card in jcards['data']:
            print('Found card: ', card.get('name'))
            # print(card)
            addCardToDB(card)
            print('------------------')
            printedcards += 1

        print('I found: ' , jcards['total_cards'],' total cards')
        print('cards printed: ', printedcards)
        
        return jcards.get(('next_page'), None)
        
    else:
        print(response)
        return None

def loadLegendsDB():
    print('Loading database: ', dbPath)
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    
    print('Creating or dropping table in DB')
    cur.executescript("""
    --sql
                    CREATE TABLE IF NOT EXISTS Cards(
                          name TEXT UNIQUE,
                          colors TEXT,
                          mana_cost INTEGER,
                          color_identity TEXT,
                          image_png TEXT
                    );
                      
    """)
    print('DB connected')
    

def addCardToDB(card):
    #write data to database
    
    name = card.get('name')
    print('name: ', name, '(type: ', type(name),')')
    colors = ''.join(card.get('colors'))
    print('colors: ', colors, '(type: ', type(colors),')')
    mana_cost = card.get('mana_cost')
    print('Mana cost: ', mana_cost, '(type: ', type(mana_cost),')')
    color_identity = ''.join(card.get('color_identity'))
    print('color_identity: ', color_identity, '(type: ', type(color_identity),')')
    image_uris = card.get('image_uris')
    # print('image_uris: ', image_uris, '(type: ', type(image_uris),')')
    image_png = image_uris.get('png')
    print('image_png: ', image_png, '(type: ', type(image_png),')')
    
    cur.execute("""
    --sql
    INSERT OR IGNORE INTO Cards (name, colors, mana_cost, color_identity, image_png) VALUES(?, ?, ?, ?, ?);
    """,(name, colors, mana_cost, color_identity, image_png))
    
    conn.commit()
    
def main():

    baseurl = 'https://api.scryfall.com/cards/'

    # Search for cardname:
    # options = 'named?exact='
    # cardname = 'marchesa the black rose'
    # url = (baseurl + options + cardname).encode()

    options = 'search?order=set&q=t:creature t:legend&dir=desc'
    url = (baseurl + options).encode()

    loadLegendsDB()
    
    count = 0

    while url is not None:
        
        url = pullPage(url)
        count += 1
        print('current count ', count)
        time.sleep(0.2)
    cur.close()
        
if __name__ == "__main__":
    main()
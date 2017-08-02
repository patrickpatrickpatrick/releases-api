import os
from lxml import html
import requests
from bs4 import BeautifulSoup
import json
import re

BANDCAMP_URL = "https://" + os.environ['BANDCAMP_LABEL'] + ".bandcamp.com/"
API_URL = "http://127.0.0.1:8000/"

def bandcamp_embed_code(id):
    return "<iframe style='border: 0; width: 500px; height: 796px;' src='https://bandcamp.com/EmbeddedPlayer/album=" + str(id) + "/size=large/bgcol=ffffff/linkcol=0687f5/package=967020329/transparent=true/'' seamless''></iframe>"

def youtube_embed_code(video):
    #it's all spread over several channels which complexes this somewhat 
    return 

def get_auth_token():
    r = requests.post("http://127.0.0.1:8000/api-token-auth/", json={"username":"patrick","password":"cv34erdf"})
    AUTH_TOKEN = json.loads(r.text)['token']

def post_auth(resource, data):
    requests.post(BANDCAMP_URL + resource, json=data, headers={"Authentication": "Token " + AUTH_TOKEN})

def scrape_videos():
    return 'uuuhhh'

def scrape_releases():
    main_page = BeautifulSoup(requests.get(BANDCAMP_URL).content, 'html.parser')
    music_grid_info = json.loads((main_page.select('.music-grid')[0]['data-initial-values']))

    for release in music_grid_info:
        release_page = BeautifulSoup(requests.get(BANDCAMP_URL + release["page_url"]).content, 'html.parser')

        if len(release_page.select('.tralbumData')) > 0:
            description =  " ".join(release_page.select('.tralbumData')[0].get_text().split())
        else:
            description = " "

        if len(release_page.select('.merchtype.secondaryText')) > 0:
            medium = " ".join(release_page.select('.merchtype.secondaryText')[0].get_text().split())
        else:
            medium = " "

        release_number = re.search('(PLZ)\d+', description).group(0) if re.search('(PLZ)\d+', description) is not None else ""

        release_json = ({
            "name": release["title"],
            "artist": release["artist"] if release["artist"] is not None else "Various Artists",
            "description": re.sub(release_number, "", description),
            "medium": medium,
            "release_number": release_number,
            "embed": bandcamp_embed_code(release["id"]),
            "release_id": release["id"],
            "url": release["page_url"],
        })

        headers = {'user-agent': 'my-app/0.0.1'}
        # r = requests.post("http://127.0.0.1:8000/releases/", json=release_json)

        merch_on_release_page = release_page.select('.tralbumCommands .buyItem')

        for merch in merch_on_release_page:
            merch_id = merch.find_all(id=re.compile("(package-price-)\w+"))

            if len(merch_id) > 0:
                merch_id = merch_id[0]['id'].split('-')[2]
            else:
                continue

            if len(merch.select('.buyItemPackageTitle.primaryText')) > 0:
                name = " ".join(merch.select('.buyItemPackageTitle.primaryText')[0].get_text().split())
            else:
                name = " ".join(merch.select("#package-title-" + merch_id)[0].get_text().split())

            if len(merch.select('.compound-button .base-text-color')) > 0:
                price = merch.select('.compound-button .base-text-color')[0].get_text()
            else:
                price = ''

            print({
             "name": release["title"] + " - " + name,
             "item": " ".join(merch.select('.merchtype.secondaryText')[0].get_text().split()),
             "merch_id": merch_id,
             "url": release["page_url"],
             "stock": len(merch.select('.buy-link')) > 0,
             "price": price
            })





def scrape_merch():
    merch_page = BeautifulSoup(requests.get(BANDCAMP_URL + 'merch').content, 'html.parser')
    all_merchandise = json.loads((merch_page.select('.merch-grid')[0]['data-initial-values']))

    for merch in all_merchandise:
        merch_json = ({
            "name": merch["title"],
            "price": merch["price"],
            "item": merch["type_name"],
            "stock": merch["quantity_available"] if (merch["quantity_available"] is not None and merch["quantity_available"] > 0) else 0,
            "url": merch["url"]
        })

        r = requests.post("http://127.0.0.1:8000/merch/", json=merch_json)

        # if re.search('album') merch["url"] 

def scrape():
    get_auth_token()
    scrape_releases()

    # scrape_merch()
    # scrape_releases()
    # scrape_videos()


    # i could use the youtube but api but all im doing is displaying these videos so why bother
    # idk ill come back to this because it's piss easy to implement anyway

if __name__ == "__main__":
    scrape()
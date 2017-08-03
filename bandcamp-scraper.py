import os
from lxml import html
import requests
from bs4 import BeautifulSoup
import json
import re
import urllib.request

BANDCAMP_URL = "https://" + os.environ['BANDCAMP_LABEL'] + ".bandcamp.com/"
API_URL = "http://127.0.0.1:8000/"
AUTH_TOKEN = json.loads(requests.post("http://127.0.0.1:8000/api-token-auth/", json={"username":"patrick","password":"cv34erdf"}).text)['token']

def bandcamp_embed_code(id):
    return "<iframe style='border: 0; width: 500px; height: 796px;' src='https://bandcamp.com/EmbeddedPlayer/album=" + str(id) + "/size=large/bgcol=ffffff/linkcol=0687f5/package=967020329/transparent=true/'' seamless''></iframe>"

def youtube_embed_code(video):
    return

def does_resource_exist(resource, json_to_send):
    # not possible to get when the resource was last updated from page so this method
    # will determine if the item needs to be updated or not...

    existing_resource = json.loads(requests.get("http://127.0.0.1:8000/" + resource + '/?' + resource + '_id=' + str(json_to_send[resource + "_id"])).text)

    if len(existing_resource) > 0:
        existing_resource_id = existing_resource[0].pop('id', None)
        existing_resource[0].pop('owner', None)

        print('*******')
        print(existing_resource[0])
        print('-------')
        print(json_to_send)
        print('*******')
        if existing_resource[0] == json_to_send:
            return True
        else:
            return False
    else:
        return False

def post_auth(resource, data):
    r = requests.post(API_URL + resource + '/', json=data, headers={"Authorization": "Token " + AUTH_TOKEN})

def delete_auth(resource, id):
    r = requests.delete(API_URL + resource + '/' + str(id), headers={"Authorization": "Token " + AUTH_TOKEN})

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
            "url": BANDCAMP_URL[:-1] + release["page_url"],
        })

        headers = {'user-agent': 'my-app/0.0.1'}
        
        post_auth('releases', release_json)

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


            images = merch.find_all(id=re.compile("packageart"))

            for idx,image in enumerate(images):
                urllib.request.urlretrieve(image['src'][:-6] + '10.jpg', merch_id + "-" + str(idx) + ".jpg")

            merch_json = {
             "name": release["title"] + " - " + name,
             "item": " ".join(merch.select('.merchtype.secondaryText')[0].get_text().split()),
             "merch_id": merch_id,
             "url": BANDCAMP_URL[:-1] + release["page_url"],
             "stock": len(merch.select('.buy-link')) > 0,
             "price": price
            }




            # post_auth('merch', merch_json)



def scrape_merch():
    merch_page = BeautifulSoup(requests.get(BANDCAMP_URL + 'merch').content, 'html.parser')
    all_merchandise = json.loads((merch_page.select('.merch-grid')[0]['data-initial-values']))

    for merch in all_merchandise:

        if merch['album_id'] != None:
            continue

        merch_json = ({
            "name": merch["title"],
            "price": str(merch["price"]),
            "item": merch["type_name"],
            "stock": True if (merch["quantity_available"] is not None and merch["quantity_available"] > 0) else False,
            "url": merch["url"],
            "merch_id": str(merch["id"])
        })

        # for idx,image in enumerate(merch['arts']):
        #     urllib.request.urlretrieve('https://f4.bcbits.com/img/00' + str(image['image_id']) + '_10.jpg', str(merch["id"]) + "-" + str(idx) + ".jpg")
        
        print(does_resource_exist('merch', merch_json))

        # print(post_auth('merch', merch_json))

def scrape():
    scrape_merch()
    # scrape_releases()
    # scrape_videos()

if __name__ == "__main__":
    scrape()
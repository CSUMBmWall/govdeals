# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

domain = "https://www.govdeals.com/"
URL = "https://www.govdeals.com/index.cfm?fa=Main.ZipSearch&zipcode=93905&miles=150&milesKilo=miles&category=00&kWordSelect=2&locationType=miles&kWord=&country=&btn_submit=Submit"

def getLinks(url):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    locations_table = soup.find('table', attrs={'class': 'searchResults'})
    anchors = locations_table.findAll('a')
    location_urls = [urljoin(domain, a['href']) for a in anchors]
    # location_urls = [urljoin(str(a['href']), domain) for a in anchors]
    return location_urls

def getInfo(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    items_table = soup.find('table', attrs={'class': 'searchResults'})
    item__rows = items_table.findAll('tr')
    for row in item__rows:
        anchors = row.findAll('a')
        if anchors:
            print('href', anchors[0].contents)
            # print('photo', urljoin(domain, anchors[0].href))
            # print('title', anchors[0].title)

location_links = getLinks(URL)
# print(location_links)

for link in location_links:
    getInfo(link)

# r = requests.get(URL)
#
# soup = BeautifulSoup(r.content, 'html.parser')
# # print(soup.prettify())
#
#
# locations_table = soup.find('table', attrs={'class': 'searchResults'})
# location_links = locations_table.findAll('a')





# for location in location_links:
#     location_url = urljoin(domain, location['href'])
#     location_page = requests.get(location_url)


# print(links)

# for row in table.findAll('td'):
#     loc = {}
#
#     try:
#         loc['url'] = row.a['href']
#
#     except:
#         loc['url'] = 'None'
#
#     locations.append(loc)
# print(locations)

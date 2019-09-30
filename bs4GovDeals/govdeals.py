# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

import requests
from bs4 import BeautifulSoup
URL = "https://www.govdeals.com/index.cfm?fa=Main.ZipSearch&zipcode=93905&miles=150&milesKilo=miles&category=00&kWordSelect=2&locationType=miles&kWord=&country=&btn_submit=Submit"
r = requests.get(URL)


soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

locations = []

table = soup.find('table', attrs= {'class': 'searchResults'})

for row in table.findAll('td'):
    loc = {}

    try:
        loc['url'] = row.a['href']

    except:
        loc['url'] = 'None'

    locations.append(loc)
print(locations)
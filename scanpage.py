import requests
from bs4 import BeautifulSoup


def ScanPage(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        links = []
        container = soup.find_all(
            'div', attrs={"class": "item poster card"})
        # print(container)
        # items = container.find('div', attrs={'class': 'item poster card'})
        for x in container:
            pageLink = x.find('a', attrs={'class': "title result"})['href']
            links.append("https://www.themoviedb.org"+pageLink)
        return links
    else:
        return [-1]

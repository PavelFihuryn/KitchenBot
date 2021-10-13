import requests
from bs4 import BeautifulSoup


def get_links():
    url = "https://www.kufar.by/l/r~minsk/stulya-ofisnye-kompyuternye"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('article')
    kitchen = []
    for link in links:
        if str(link.find('span'))[6:-7].split(',')[0] == 'Сегодня':
            kitchen.append(link.find('a').get('href'))
    return kitchen


if __name__ == '__main__':
    print(*get_links(), sep='\n')

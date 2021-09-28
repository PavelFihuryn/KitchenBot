import requests
from bs4 import BeautifulSoup


def get_links():
    url = "https://www.kufar.by/l/r~minsk/kuhni?sort=lst.d&cnd=1&cur=BYR&query=%D0%BA%D1%83%D1%85%D0%BD%D1%8F&size=42"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    links = soup.find('article', class_='kf-iwJ-a69a6')
    if links:
        links_list = links.find_all('a', class_='kf-wwee-3f4fa')
    else:
        return []
    kitchen = []
    for link in links_list:
        if str(link.find('span'))[6:-7].split(',')[0] == 'Сегодня':
            kitchen.append(link.get('href'))
    return kitchen


if __name__ == '__main__':
    print(*get_links(), sep='\n')

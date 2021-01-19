import requests
from bs4 import BeautifulSoup
import threading
import time

url = 'https://www.gry-online.pl/newsroom/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
divList = soup.findAll('div', {'class': 'box'})
threads = []


def function(div):
    link = div.find('a').get('href')
    print('Link: ' + 'https://www.gry-online.pl' + link)
    title = div.find('h5').getText()
    print('Title: ' + title)
    allP = div.findAll('p')
    for p in allP:
        print(p.text)
    print('\n')


def main():
    counter = 0
    for div in divList:
        if counter == 10:
            break
        t = threading.Thread(target=function, args=(div,))
        threads.append(t)
        t.start()
        time.sleep(0.001)
        counter += 1


if __name__ == '__main__':
    main()

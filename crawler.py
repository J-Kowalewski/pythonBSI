import requests
from bs4 import BeautifulSoup
import threading
import time
"""
    :author: Jakub Kowalewski
"""

url = 'https://www.gry-online.pl/newsroom/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
divList = soup.findAll('div', {'class': 'box'})
threads = []


def crawl(div):
    """
    gets hyperlink, title, author, date and summary of article from https://www.gry-online.pl
    :param div: 1 div element from divList where divList = soup.findAll('div', {'class': 'box'})
    :return: nothing
    """
    link = div.find('a').get('href')
    print('Link: ' + 'https://www.gry-online.pl' + link)
    title = div.find('h5').getText()
    print('Title: ' + title)
    allP = div.findAll('p')
    for p in allP:
        print(p.text)
    print('\n')


def main():
    """
    for every element of divList (maximum of 10) new thread is created and function crawl is called
    program waits 0.001s for each thread to avoid problems with printing values
    :return: nothing
    """
    counter = 0
    for div in divList:
        if counter == 10:
            break
        t = threading.Thread(target=crawl, args=(div,))
        threads.append(t)
        t.start()
        time.sleep(0.001)
        counter += 1


if __name__ == '__main__':
    main()
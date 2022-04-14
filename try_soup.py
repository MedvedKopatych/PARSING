import requests
import lxml.html
from bs4 import BeautifulSoup

url = 'https://flyeasy.co/opapi/-fe3-dt1--ht2--ht3--ht4-ctp:magellanjets_list:-/' \
      '578526bdf6c494c11477ab06/'

headers = {
    'user-agent':  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'
}

def parse_data(url, headers):
    titles = []
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    print(response)


    soup = BeautifulSoup(html, 'lxml')
    print(soup.encode('utf-8'))
    items = soup.find_all('div', attrs = {'class' : 'acTitle'})
    print(items)
    for item in items:
        span = item.find_next('span')
        if span:
            span.replace_with('')
        titles.append(item.text.strip())
        print(item)
    print(titles)





parse_data(url, headers)
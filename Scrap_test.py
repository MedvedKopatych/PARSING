import requests
import lxml.html
import time
from fake_useragent import UserAgent


def parse_data(url):
    titles = []
    try:
        ua = UserAgent()
        ua.chrome
        response = requests.get(url)
        print(response)
        html = response.content
        html[:1000]
        print(html)
    except:
        return
    tree = lxml.html.document_fromstring(response.text)
    for key, value in response.request.headers.items():
        print(key + ": " + value)
    for item in tree.xpath('//*[contains(@class, "acTitle")]'):
        title = item.xpath(".//span/text()")
        print(title)
        titles.append(title)
        print(titles)
        print(len(titles))


def main():
    url = 'https://flyeasy.co/opapi/-fe3-dt1--ht2--ht3--ht4-ctp:magellanjets_list:-/578526bdf6c494c11477ab06/'
    print(url)
    parse_data(url)
    time.sleep(2)


if __name__ == "__main__":
    main()

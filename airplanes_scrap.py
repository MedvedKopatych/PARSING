import requests
from lxml import etree
import lxml.html
import csv


def get_name(url):
    return url.split("/")[2]


def parse_data(url):
    try:
        response = requests.get(url)
        print(response)
    except:
        return
    tree = lxml.html.document_fromstring(response.text)
    text_aicraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/h2/a/text()')
    price_aicraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/div[1]/text('')')
    price = price_aicraft[0] if price_aicraft else "N/A"
    year_aicraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/div[3]/div[1]/div[1]/ul/li[1]/text()')
    s_n_aicraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/div[3]/div[1]/div[1]/ul/li[2]/text()')
    time_aicraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/div[3]/div[1]/div[1]/ul/li[3]/text()')
    place_aircraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/div[2]/text()')
    dealer_aircraft = tree.xpath('//*[contains(@id, "item_card")]/div/div[4]/div/div[2]/b/text()')
    price_empty = tree.xpath('//*[@id="item_card_361757"]/div/div[4]/div/div[1]/text()')
    print(text_aicraft)
    print(len(text_aicraft))
    print(price_aicraft)
    print(len(price_aicraft))
    print(price_empty)
    """name = get_name(url)
    with open("%s.csv" % name, "w", newline='') as csv_file:
        write = csv.writer(csv_file)
    
        for i in range(len(price_aicraft)):
            print(text_aicraft[i])
            print(price_aicraft[i])
            print(year_aicraft[i])
            print(s_n_aicraft[i])
            print(time_aicraft[i])
            print(place_aircraft[i])
            print(dealer_aircraft[i])
            write.writerow([text_aicraft[i]])"""


def main():
    """num_of_page = 26
    for i in range(1, num_of_page+1):"""
    url = 'https://www.avbuyer.com/aircraft/private-jets/page-13'
    print(url)
    parse_data(url)


if __name__ == "__main__":
    main()

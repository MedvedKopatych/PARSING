import requests
import lxml.html
import time
import sys
import pandas as pd

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def parse_data(url):
    titles = []
    prices = []
    years = []
    total_times = []
    serial_numbers = []
    locations = []
    dealers = []
    links = []
    try:
        response = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(response.text)
    for item in tree.xpath('//*[contains(@class, "listing-item")]'):
            title = item.xpath(".//h2/a/text()")[0]
            price = item.xpath('.//*[contains(@class, "price")]/text()')
            price = price[0] if price else "N/A"
            year_aircraft = item.xpath('.//ul/li[1]/text()')[0]
            serial_number = item.xpath('.//ul/li[2]/text()')[0]
            total_time = item.xpath('.//ul/li[3]/text()')[0]
            location = item.xpath(".//div[2]/text()")[0]
            dealer = item.xpath(".//b/text()")[0]
            link = "https://www.avbuyer.com" + item.xpath(".//h2/a")[0].attrib['href']
            titles.append(title)
            prices.append(price)
            years.append(year_aircraft.strip('Year'))
            total_times.append(total_time.strip('Total Time'))
            serial_numbers.append(serial_number.strip('S/N'))
            locations.append(location.strip(', For Sale by'))
            dealers.append(dealer)
            links.append(link)




            output = pd.DataFrame({"Make": titles,
                           "Price": prices,
                           "Year": years,
                           "Serial Number": serial_numbers,
                           "Time": total_times,
                           "Location": locations,
                           "Dealer": dealers,
                           "Link": links})

            output.to_excel(r'TESTAVbuyer.com.xlsx', sheet_name='avbuyer.com', index=False)
    



def main():
    for i in range(23, 26):
        url = 'https://www.avbuyer.com/aircraft/private-jets/page-' + str(i)
        print(url)
        parse_data(url)
        i += 1
        time.sleep(2)


if __name__ == "__main__":
    main()


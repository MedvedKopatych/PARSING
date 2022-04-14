import requests
import lxml.html
import time
import sys
import pandas as pd

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def main():
    dfFinal = pd.DataFrame()

    for i in range(1, 30):
        url = 'https://www.avbuyer.com/aircraft/private-jets/page-' + str(i)
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
        for item in tree.xpath('//*[contains(@id, "item_card")]'):
            if item in tree.xpath('//*[contains(@class, "listing-item")]'):
                title = item.xpath(".//h2/a/text()")
                title = title[0] if title else item.xpath(".//h2/text()")[0]
                price = item.xpath('.//*[contains(@class, "price")]/text()')
                price = price[0] if price else "N/A"
                year_aicraft = item.xpath('.//ul/li[1]/text()')
                year_aicraft = year_aicraft[0] if year_aicraft else ""
                serial_number = item.xpath('.//ul/li[2]/text()')
                serial_number = serial_number[0] if serial_number else ""
                total_time = item.xpath('.//ul/li[3]/text()')
                total_time = total_time[0] if total_time else ""
                location = item.xpath(".//div[2]/text()")
                location = location[0] if location else ""
                dealer = item.xpath(".//b/text()")
                dealer = dealer[0] if dealer else item.xpath(".//p/text()")[0]
                adlink = item.xpath(".//h2/a")
                adlink = adlink[0].attrib['href'] if adlink else ""
                link = "https://www.avbuyer.com" + adlink
                titles.append(title.strip())
                prices.append(price)
                years.append(year_aicraft.strip('Year'))
                total_times.append(total_time.strip('Total Time'))
                serial_numbers.append(serial_number.strip('S/N'))
                locations.append(location.strip(', For Sale by').strip())
                dealers.append(dealer)
                links.append(link)

        output = pd.DataFrame({"Make": titles,
                           "Price": prices,
                           "Year": years,
                           "Serial Number": serial_numbers,
                           "Time": total_times,
                           "Location": locations,
                           "Dealer": dealers,
                           "Link": links,
                               })
        dfFinal = dfFinal.append(output)
        print(url)
        i += 1
        time.sleep(2)

    writer = pd.ExcelWriter('Scraped Aicraft_sites.xlsx')
    dfFinal.to_excel(writer, sheet_name='avbuyer.com', index=False)
    for column in dfFinal:
        column_width = max(dfFinal[column].astype(str).map(len).max(), len(column))
        col_idx = dfFinal.columns.get_loc(column)
        writer.sheets['avbuyer.com'].set_column(col_idx, col_idx, column_width)
    writer.save()

main()
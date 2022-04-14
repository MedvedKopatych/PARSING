import requests
from lxml import etree
import lxml.html
import csv


def get_name(url):
    return url.split("/")[-1].split(".")[0]
def parse_data(url):
    try:
        response = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(response.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    name = get_name(url)
    with open("%s.csv" % name, "w", newline='') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            print(text_original[i])
            write.writerow([text_original[i]])
            write.writerow([text_translate[i]])


def main():
    parse_data("https://www.amalgama-lab.com/songs/m/modern_talking/angie_s_heart.html")


if __name__ == "__main__":
    main()
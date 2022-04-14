import xml

import requests
import lxml.html
from xml.dom.minidom import parse, parseString
help(xml.dom.minidom)
url = 'https://flyeasy.co/opapi/-fe3-dt1--ht2--ht3--ht4-ctp:magellanjets_list:-/' \
      '578526bdf6c494c11477ab06/'

headers = {
    'user-agent':  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'
}
response = requests.get(url, headers=headers)
print(response)
html = response.content.decode('utf-8')
print(type(html))
print(html)
dom = xml.dom.minidom.parseString(html, parser=None)
print(dom)
def parse_data(url, headers):
    titles = []
    try:
        pass
    except:
        return
    tree = lxml.html.document_fromstring(response.text)
    for item in tree.xpath('//*[contains(@class, "fa fa-plane")]'):
        title = item.xpath(".//text()")
        print(title)
        titles.append(title)
    







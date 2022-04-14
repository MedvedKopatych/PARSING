import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.avbuyer.com/aircraft/private-jets/page-13")
soup = BeautifulSoup(req.text, "lxml")

blocks = soup.find_all("div", class_="price")
prices=[]
for block in blocks:

    if block:
        price = block.text
        print(price)
        prices.append(price)
print(prices)
print(len(prices))



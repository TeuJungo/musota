# pip install BeautifulSoup
# pip install requests

from bs4 import BeautifulSoup

import requests

url_from = "https://www.google.com/search?q=notaco+do+dolar"





response = requests.get(url_from)

html = response.text

bso4 = BeautifulSoup(html,'html.parser')

# print(bso4.prettify())

print(bso4.find("title"))


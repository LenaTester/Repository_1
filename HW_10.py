from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"
next_page_url = url
counter = 0

while True:
    print(counter, next_page_url)
    counter += 1
    r = requests.get(next_page_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    next_page_link = soup.find("li", {"class": "next"})
    if not next_page_link:
        break
    next_page_url = url + next_page_link.a["href"]

print(counter)
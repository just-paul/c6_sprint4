from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# print(soup.prettify())

# match = soup.find('div', class_ = 'footer').text

for article in soup.find_all('div', class_ = 'article'):
# print(article)

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
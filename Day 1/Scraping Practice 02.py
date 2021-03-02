from bs4 import BeautifulSoup
import requests
pip install bs4


source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'html.parser')

print(soup.prettify())

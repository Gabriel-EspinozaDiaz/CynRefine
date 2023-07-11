from bs4 import BeautifulSoup
import requests as req

page = req.get('http://parts.igem.org/Part:BBa_K3237027')
soup = BeautifulSoup(page.text,'html.parser')
print(soup.prettify())
import scraping
import iterations
import os

'''

'''

scrape1 = scraping.Scraper('http://parts.igem.org/Part:BBa_C0040')
scrape2 = scraping.Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001')

scrape1.get_content()
scrape1.write_content('ex1')
print(scrape1.content_get_data())
scrape2.get_content()
scrape2.write_content('ex2')
print(scrape2.content_get_data())
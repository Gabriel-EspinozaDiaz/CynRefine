import scraping
import iterations
import os

'''

'''

scrape1 = scraping.Scraper('http://parts.igem.org/Part:BBa_C0040')
scrape2 = scraping.Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001')

scrape1.write_content('ex1')
print(scrape1.scrape_text())
scrape2.write_content('ex2')
print(scrape2.scrape_text())
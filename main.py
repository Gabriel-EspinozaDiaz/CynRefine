import scraping
import iterations
import os

'''

'''

scrape1 = scraping.Scraper('http://parts.igem.org/Part:BBa_C0040')

scrape1.get_content()
print(scrape1.check_fasta())
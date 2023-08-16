from scraping import Scraper
import iterations
import os

'''

'''

scrape1 = Scraper('http://parts.igem.org/Part:BBa_C0040')
scrape2 = Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001')
trial = iterations.Trial()

trial.page_as_csv('example1',scrape1)
trial.page_as_csv('example2',scrape2)

from scraping import Scraper
import iterations
import time

'''

'''

scrape1 = Scraper('http://parts.igem.org/Part:BBa_C0040')
scrape2 = Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001')
iterator = iterations.Iterator()

iterator.get_size_csvs('allurls.txt')


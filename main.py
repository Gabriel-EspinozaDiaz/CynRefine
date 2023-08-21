from scraping import Scraper
import iterations
import time

'''

'''

scrape1 = Scraper('http://parts.igem.org/Part:BBa_C0040')
scrape2 = Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001')
scrape3 = Scraper('http://parts.igem.org/Part:BBa_B1002')
scrape4 = Scraper('http://parts.igem.org/Part:BBa_B1102')
iterator = iterations.Iterator()

#iterator.get_size_csvs('allurls.txt',60)


from scraping import Scraper
import iterations
import time

'''

'''

#scrape1 = Scraper('http://parts.igem.org/Part:BBa_C0040') EXAMPLE
#scrape2 = Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001') EXAMPLE
#scrape3 = Scraper('http://parts.igem.org/Part:BBa_B1002') FIRST OCCURENCE OF RFC, CAUSED ERROR AT REGISTRY STAR SCRAPE
#scrape4 = Scraper('http://parts.igem.org/Part:BBa_B1102') FIRST OCCURENCE OF 'NO RESULTS' REPSONSE, CAUSED ERROR AT SAMPLE EXPERIENCE SCRAPE
scrape5 = Scraper('http://parts.igem.org/Part:BBa_C0012')
iterator = iterations.Iterator()

scrape5.write_content('spadoof')

#iterator.get_size_csvs('allurls.txt',73)


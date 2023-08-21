from scraping import Scraper
import iterations
import time

'''

'''

scrape1 = Scraper('http://parts.igem.org/Part:BBa_C0040')
scrape2 = Scraper('http://parts.igem.org/wiki/index.php?title=Part:BBa_K2607001')
trial = iterations.Trial()

trial.page_as_csv('ex1',scrape1)
time.sleep(1)
trial.page_as_csv('ex2',scrape2)
time.sleep(1)
trial.check_size(scrape1)
time.sleep(1)
trial.check_size(scrape2)
time.sleep(1)

trial.dual_check_size('shortlist.txt')


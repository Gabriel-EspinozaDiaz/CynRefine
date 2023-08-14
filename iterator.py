import scraper
import os
import sys
'''

'''

class Iterator:

    def get_size(url_list):
        '''
        Takes a list of urls and scrapes each one, determining required to store all of their data
        '''
        total = 0
        file = open(url_list,'r')
        for n in file.readlines():
            total += sys.getsizeof(scraper.Scraper(str(n)))
        print(total)
import scraping
import os
import sys
'''

'''

class Iterator:

    def get_size_url(url_list):
        '''
        Takes a list of urls and scrapes each one, determining required to store all of their data
        '''
        urls = []
        file = open(url_list,'r')
        for n in file.readlines():
            urls.append(n)
        print(urls)
        print(sys.getsizeof(urls))
    
    def get_size_texts(url_list):
        '''
        Takes a list of urls and scrapes each one, determining required to store all of their data
        '''
        total = 0
        file = open(url_list,'r')
        for n in file.readlines():
            total += sys.getsizeof(scraping.Scraper(str(n)))
        print(total)
    
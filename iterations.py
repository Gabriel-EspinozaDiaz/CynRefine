from scraping import Scraper
import os
import sys
import time
import csv
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
        file.close()
    
    def get_size_texts(url_list):
        '''
        Scrapes all web contents used by 
        '''
        total = 0
        file = open(url_list,'r')
        
        os.remove("demofile.txt")
        print(total)
        file.close()

class Trial:
    '''
    These are methods mirror those of Iterator, but only operate on a single page, rather than all 24,098 pages. 
    This is just for testing on the scope of a single file using a similar format to that of the iterator without the risk of blowing up my laptop. 
    '''

    def page_as_csv(url,name,scrape):
        with open(name+'.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['part','part_status','sample_status','experience','uses','twins','authors','team','date','text'])
            csv.writer(file).writerow(scrape.package_for_csv())





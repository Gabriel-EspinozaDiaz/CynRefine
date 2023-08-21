from scraping import Scraper
import os
import sys
import time
import csv
import numpy as np
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
        urls = []
        #Read all urls into a list
        file = open(url_list,'r')
        for n in file.readlines():
            urls.append(n)
        file.close()
        #Write each


        file.close()

class Trial:
    '''
    These are methods mirror those of Iterator, but only operate on a single page, rather than all 24,098 pages. 
    This is just for testing on the scope of a single file using a similar format to that of the iterator without the risk of blowing up my laptop. 
    '''

    def page_as_csv(self,name,scrape):
        with open(name+'.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['part','part_status','sample_status','experience','uses','twins','authors','team','date','text'])
            csv.writer(file).writerow(scrape.package_for_csv())
    
    def check_size(self,scrape):
        with open('temp_file.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['part','part_status','sample_status','experience','uses','twins','authors','team','date','text'])
            csv.writer(file).writerow(scrape.package_for_csv())
        print('\nTEMPORARY FILE INITIALISED\n')
        size = os.path.getsize('temp_file.csv')
        print(f'filesize: {size} bytes')
        os.remove('temp_file.csv')
        print('\nTEMPORARY FILE DELETED')


    def dual_check_size(self,url_list):
        total = 0
        urls = []
        #Store urls in list
        file = open(url_list,'r')
        for n in file.readlines():
            urls.append(n.replace('\n',''))
        file.close()
        #Loop through 
        for n in range(len(urls)):
            with open('temp_file.csv','w',newline='') as file:
                url = urls[n]
                scrape = Scraper(url)
                csv.writer(file).writerow(scrape.package_for_csv())
                time.sleep(1)
            print('\nTEMPORARY FILE INITIALISED\n')
            total += os.path.getsize('temp_file.csv')
            print(f'current repository size: {total} bytes')
            os.remove('temp_file.csv')
            print('\nTEMPORARY FILE DELETED')





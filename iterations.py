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
    
    def get_size_csvs(self,url_list,sPoint=1):
        '''
        Takes an starting point (sPoint, int) and txt file name as parameters (str)
        Checks all urls listed in the file, writing all content into a csv file and then 
        Based on the current size of the repository and the need for breaks to prevent getting kicked off the website, this method takes 6-8 hours to complete
        On account of that, sPoint can be used to start the process at a desired file. 
        The method prints the name and line number of the url in url_list. If you want to skip over files, use the last printed file # as sPoint 
        '''
        total = 0
        urls = []
        #Store urls in list
        file = open(url_list,'r')
        for n in file.readlines():
            urls.append(n.replace('\n',''))
        file.close()
        #Loop through 
        for n in range(sPoint-1,len(urls)):
            with open('temp_file.csv','w',newline='') as file:
                url = urls[n]
                scrape = Scraper(url)
                csv.writer(file).writerow(scrape.package_for_csv())
            total += os.path.getsize('temp_file.csv')
            print(f'current repository size: {total} bytes')
            os.remove('temp_file.csv')
            print(f'file {n+1} ({url}) removed\n')
            #Give the website a bit of time in between requests to avoid being blocked
            time.sleep(1)

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





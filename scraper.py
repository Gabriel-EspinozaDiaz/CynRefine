import requests
import re
from bs4 import BeautifulSoup

'''
This is the scraper module. It accepts a url and 
'''


class Scraper:
    def __init__(self,url):
        if type(url) != str:
            raise TypeError("url must be in string form")
        self.url = url
    
    def check_url(self):
        response = requests.get(self.url)
        # Determine whether the website exists 
        if response.status_code == 200: 
            print("response successful. The website exists.")
        else:
            print("response failed.")
        
    def get_content(self):
        '''
        retrieves information from the website
        '''
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.content = soup
    
    def present_content(self):
        return self.content.prettify()
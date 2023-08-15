import requests
import re
from bs4 import BeautifulSoup
import urllib.request

'''
This is the scraper module. It accepts a url and 
'''

class Scraper:
    def __init__(self,url):
        if type(url) != str:
            raise TypeError("url must be in string form")
        self.url = url
    
    def check_url(self):
        '''
        Ensures that the url exists
        '''
        response = requests.get(self.url)
        # Determine whether the website exists 
        if response.status_code == 200: 
            print("response successful. The website exists.")
        else:
            print("response failed.")
        
    def get_content(self):
        '''
        Retrieves information from the website
        '''
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.content = soup
    
    def content_technical(self):
        '''
        Shows the content as it's stored. Better for technical use. 
        '''
        return self.content
    
    def content_for_user(self):
        '''
        Presents the content with newlines and indents inserted. 
        This modifies the appearance, making information easier to digest. 
        '''
        return self.content.prettify()
    
    def content_get_data(self,name):
        '''
        Once this method is finished, it will break down a page by 
        '''
        end = 'Part:BBa_'
        basic = self.content.get_text()
        basic = basic[basic.find('main page'):]
        prelude = basic[:basic.find(end)]
        # Determines all tag data from status box information (see info on status boxes at http://parts.igem.org/Help:Part_Status_Box)
        part_status = self.get_part_status(prelude)
        #sample_status = self.get_sample_status(prelude)
        #experience = self.get_experience(prelude)
        #uses = self.get_uses(prelude)
        #twins = self.get_twins(prelude)
    
        with open(name+'.txt', 'w') as f:
            f.write(basic)
        return part_status
    
    def get_part_status(self,text):
        start1_2 = 'Released' #This counts for Released or Released HQ entries
        start3 = 'Not Released'
        start4 = 'Discontinued'
        if start4 in text:
            status = start4
        elif start3 in text:
            status = start3
        elif start1_2 in text:
            status = start1_2
        else:
            print('Error occured: no release status found')
        return status
    
    def get_sample_status(self,text):
        return 0
    
    def get_experience(self,text):
        return 0
    
    def get_uses(self,text):
        return 0
    
    def get_twins(self,text):
        return 0


    def check_fasta(self):
        '''
        Every page with an attached sequence has a counterpart page under the format "http://parts.igem.org/fasta/parts/BBa_xxxxx"
        If said page exists, this method checks that and extracts the sequence and returns it
        If not the page returns False
        '''
        fasta = 'http://parts.igem.org/fasta/parts/BBa_'+re.findall("BBa_.+",self.url)[0][4:]
        response = requests.get(fasta)
        if response.status_code == 200: 
            data = ''
            for line in list(urllib.request.urlopen(fasta))[1:]:
                data += str(line)
                sequence = ''
            #Removes byte markers
            for c in data:
                if c == 'b' or c == "'":
                    continue
                sequence += c
            return sequence
        else: 
            return False
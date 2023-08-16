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
        #Scrub off multiple consecutive newlines and 
        content = re.sub(r'(\n\s*)+\n', '\n\n',soup.get_text())
        self.content = content
    
    def write_content(self,name):
        with open(name+'.txt', 'w') as f:
            f.write(self.content)
    
    def content_get_data(self):
        '''
        This scrapes
        '''
        #Creates a smaller version of the file for reading in information from the status box
        digest = self.content[self.content.find('main page'):]
        digest = digest[:digest.find('Part:BBa_')].lower()

        # Determines all tag data from status box information (see info on status boxes at http://parts.igem.org/Help:Part_Status_Box)
        part_status = self.get_part_status(digest)
        sample_status = self.get_sample_status(digest)
        experience = self.get_experience(digest,sample_status)
        uses = self.get_uses(digest,experience)
        twins = self.get_twins(digest)

        #Reading in authors and date
        authors = self.get_authors()
        org = self.get_org()
        date = self.get_date()


        return [part_status,sample_status,experience,uses,twins,authors,org,date]
    
    def get_part_status(self,text):
        if 'discontinued' in text:
            return 'Discontinued'
        elif 'not released' in text:
            return 'Not Released'
        elif 'released hq' in text:
            return 'Released HQ'
        elif 'released' in text:
            return 'Released'
        else:
            print('Error occured: no release status found')
            return ''
    
    def get_sample_status(self,text):
        if 'sample in stock' in text:
            return 'Sample in Stock'
        elif "it's complicated" in text:
            return "It's Complicated"
        elif 'not in stock' in text:
            return 'Not in Stock'
        elif 'informational' in text:
            return 'Informational'
        else:
            print('Error occured: no sample status found')
            return ''
    
    def get_experience(self,text,sample):
        #Requires the sample status due to re being needed for registry star counting
        if 'registry star' in text:
            sample = sample.lower()+'\n'
            result = re.findall(sample+r'(\d*) registry star',text)[0]
            if int(result) == 1:
                return result+' Registry Star'
            else:
                return result+' Registry Stars'
        elif 'works' in text:
            return 'Works'
        elif 'issues' in text:
            return 'Issues'
        elif 'fails' in text:
            return 'Fails'
        else:
            print('Error occured: no sample status found')
            return ''
    
    def get_uses(self,text,exp):
        #Requires the experience due to re being needed for use counting
        if 'not used' in text:
            return 'Not Used'
        elif 'use' in text:
            exp = exp.lower()+'\n'
            result = re.findall(exp+r'(\d*) use',text)[0]
            if int(result) == 1:
                return result+' Use'
            else:
                return result+' Uses'
        else:
            print('Error occured: no use status found')
            return ''
        return 0
    
    def get_twins(self,text):
        if 'twins' in text:
            return 'Contains Twins'
        else:
            return 'No Twins'

    def get_authors(self):
        return re.findall(r'Designed by: (.*\w).*Group:',self.content)[0]
    
    def get_org(self):
        return re.findall(r'Group: (.*?)\s',self.content)[0]
        
    def get_date(self):
        return re.findall(r'\((.*)\)',self.content)[0]

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
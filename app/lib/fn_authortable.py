import os,sys,time

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class authortable:
    debug =1
    
    def __init__(self,element):
        self.soup = element

        
    def parseUserLinkQueryString(self,value):
        if self.debug == 1: print("-> parseUserLinkQueryString")
        if self.debug == 1: print(value)
        parse_result = urlparse(value)
        dict_result = parse_qs(parse_result.query)
        return dict_result['id'][0]
    

    def parseInfoTable(self):
        if self.debug == 1: print("parseInfoTable")
        table = self.soup.find("table")
        div = table.find_all('div')

        tds = div[0].find_all('font')

        lines = div[1].text.split("\n")
        for line in lines:
            if line != "":
                if "Date:" in line:
                    self.date =line.split(": ")[1]
                    #print(self.date)
                    datetime_object = datetime.strptime(self.date, '%Y-%m-%d %H:%M')
                    print("SET self.date  "+str(datetime_object))
                    self.date = datetime_object  # printed in default format
        
        #exit()
        #print(div)
        #print(tds)
        # Author:
        # Author Website:
        # Requirements:
        # Version:
        # Signed:
        # Short description: 
        # 
        #print(div[0].find(string="Author:"))
        #print(div[0])
        
        


        authorLink = div[0].find(string="Author:").findNext('a')['href']
        if authorLink != "":
            #print(authorLink)
            try:
                armaholicAuthorId = self.parseUserLinkQueryString(authorLink)
                self.authorid = armaholicAuthorId
                print("SET self.authorid "+self.authorid )
            except:
                print("No authorLink found.")
        
        div[0].find("br").extract()
        #exit()
        #div.
        #x = div.find(string="Requirements:")
        lines = div[0].text.split("\n")
        for line in lines:
            if line != "":
                if "Author:" in line:
                    self.author =line.split(": ")[1]
                    print("SET self.author "+self.author)
                elif "Author Website:" in line:
                    self.author_website =line.split(": ")[1]
                    print("SET self.author_website  "+self.author_website)
                elif "Requirements:" in line:
                    self.requirements =line.split(": ")[1]
                    print("SET self.requirements  ")
                elif "Version" in line:
                    self.version =line.split(": ")[1]
                    print("SET self.version  "+self.version)
                elif "Signed:" in line:
                    self.signed =line.split(": ")[1]
                    print("SET self.signed  "+self.signed)
                elif "Short description:" in line:
                    try:
                        self.short_description = line.split(":  ")[1]
                        print("SET self.short_description  "+self.short_description)
                    except Exception as e:
                        print("No short_description.")
        
        
        

        #exit()
        #b_tag = address.parent
        #print(b_tag)
        #td_tag = b_tag.parent
        #next_td_tag = td_tag.findNext('td')
        #print (next_td_tag.contents[0])
        #exit()
    
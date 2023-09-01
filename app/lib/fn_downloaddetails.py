import os, sys,time
from urllib.parse import urlparse, parse_qs

from lib import fn_linkhelper

class downloaddetails:
    debug=1

    def __init__(self,element):
        self.soup = element
        self.linkhelper = fn_linkhelper.linkhelper()
    
    def parseDownloadFileLink(self,value):
        parse_result = urlparse(value)
        dict_result = parse_qs(parse_result.query)
        try :
            parse_result= dict_result['download_file'][0]
        except Exception as e:
            raise NameError('no download_file parameter found!')
            print(e)
            exit()

        s_parse_result=urlparse(parse_result)
        parts = os.path.split(s_parse_result.path)
        
        
        self.armaholicpath = parts[0]
        if self.debug == 1 : print("SET self.armaholicpath "+self.armaholicpath)
        
        self.armaholicfilename = parts[1]
        if self.debug == 1 : print("SET self.armaholicfilename "+self.armaholicfilename)
        
        
        return parts
    
    def parseElement(self):
    #
        # Get the download link from the form
        #
        #if self.debug == 1 : print("FIND download link")
        try:
            forms = self.soup.find_all("form")
            #print( forms[0].get('action'))
            # store the results  

            self.armaholicDownloadLink = self.linkhelper.getHrefLink( forms[0].get('action') )
            if self.debug == 1 : print("SET self.armaholicDownloadLink "+self.armaholicDownloadLink)
            

            # remove the form div.
            #formdiv.extract()
            #print(".... "+self.armaholicDownloadLink)
            #
            # populate self.armaholicpath  self.armaholicfilename
            #
            self.parseDownloadFileLink(self.armaholicDownloadLink)
            self.parseDownloadInfo()
            
        except Exception as e:
            print("****Exception "+str(e))
            #print("No download link found!")
            #time.sleep(5)
            raise Exception("No download link found!")
            #print(self.soup)
            #exit("")
            #input("Continue after Exception")
            #exit("..fin..")
        
        
        

    def parseDownloadInfo(self):

        tables = self.soup.findChildren('table')
        my_table = tables[0]
        
        rows = my_table.findChildren(['th', 'tr'])
        for row in rows:
            next
        
        infoparts = row.text.replace("Type :","").strip().replace("\xa0","").replace("Downloaded","").replace("Size : ","").replace("Report archive:","").replace("times","").replace("Troubles downloading from Armaholic?","").split(":") 

        downloadSizeParts = infoparts[0].strip().split(" ")
        if downloadSizeParts[1]=="MB":
            downloadSize = float(downloadSizeParts[0])
        else:
            raise Exception("Download size not in MB!")

        if self.debug == 1 : print("SET self.downloadsize "+str(downloadSize))
        self.downloadsize=downloadSize


        downloadCount= int(infoparts[1].strip())
        if self.debug == 1 : print("SET self.downloadcount "+str(downloadCount))
        self.downloadcount=downloadCount

        
         
        
        
        #downloadcount=
        
        
        #exit()
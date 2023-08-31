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
        self.armaholicfilename = parts[1]
        return parts
    
    def parseElement(self):
    #
        # Get the download link from the form
        #
        if self.debug == 1 : print("FIND download link")
        try:
            forms = self.soup.find_all("form")
            print( forms[0].get('action'))
            # store the results  

            self.armaholicDownloadLink = self.linkhelper.getHrefLink( forms[0].get('action') )

            # remove the form div.
            #formdiv.extract()
            #print(".... "+self.armaholicDownloadLink)
            #
            # populate self.armaholicpath  self.armaholicfilename
            #
            parse_result = self.parseDownloadFileLink(self.armaholicDownloadLink)
            print("SET self.armaholicfilename "+self.armaholicfilename)
            print("SET self.armaholicpath "+self.armaholicpath)
        except Exception as e:
            print("****Exception "+str(e))
            print("No download link found!")
            time.sleep(5)
            #input("Continue after Exception")
            #exit("..fin..")


        tables = self.soup.findChildren('table')
        my_table = tables[0]
        rows = my_table.findChildren(['th', 'tr'])
        for row in rows:
            next
        fileInfo =row.text.replace("Type :","").strip().split(" \xa0 ")
        print("SET self.downloadsize "+fileInfo[0])
        self.downloadsize=fileInfo[0]
        print("SET self.downloadcount "+fileInfo[1])
        self.downloadcount=fileInfo[1]
        #exit()
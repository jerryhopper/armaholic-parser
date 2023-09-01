from lib import fn_authortable
from lib import fn_downloaddetails
from lib import fn_contentarea
import time


class extractor:
    debug=1
    content=False
    page_title_element=None
    foundLayout=False
    


    def __str__(self) -> str:
        
        return  "---------fn_dataextractor.extractor()\n"\
                #"page_is_valid="+str(self.page_is_valid) +"\n"\
                #"page_template="+str(self.page_template) +"\n"\
                #"armaholicSection="+str(self.armaholicSection) +"\n"\
                #"page_html_title="+str(self.page_head_title) +"\n"\
                #"\n"

        #pass

    def __init__(self,layoutparser):

        # self.layoutparser.armaholicId)
        # self.layoutparser.foundLayout)
        # self.layoutparser.page_head_title)
        # self.layoutparser.armaholicSection)
        # self.layoutparser.result)
        if layoutparser.result == None:
            print(layoutparser)
            print("** Check fn_layoutparser if self.result is being populated with result from self.layout?(????)")
            raise Exception("NO RESULT FROM LAYOUTPARSER!")
        
        self.layoutparser = layoutparser
        self.mysoup = layoutparser.result

        self.cleanup()
        
    
    def extract(self):
        # call the specific layout function.
        do = f"layout_{self.layoutparser.foundLayout}"
        
        # this will call function self.layout_?()
        if hasattr(self, do) and callable(getattr(self, do)):
            func = getattr(self, do)
            func()

    

    def cleanup(self):
        # Do some cleaning.

        # remove div.footer
        try:
            self.mysoup.find("div", {"class": ["footer"]}).extract()
        except Exception as e:
            pass
        
        # remove div.footer
        try:
            self.mysoup.find("div", {"class": ["pageText"]}).extract()
        except Exception as e:
            pass

        # remove div.footer
        try:
            self.mysoup.find("div", {"class": ["rating"]}).extract()
        except Exception as e:
            pass

        # remove div#noscript
        try:
            self.mysoup.find("div", {"id": "noscript"}).extract()
        except Exception as e:
            pass
        
        # remove div#user
        try:
            self.mysoup.find("div", {"id": "user"}).extract()
        except Exception as e:
            pass

        # remove div#user
        try:
            self.mysoup.find("div", {"id": "nav"}).extract()
        except Exception as e:
            pass


    def layout_5(self):
        print("layout_5")
        exit()

    def layout_4(self):
        print("layout_4")
        
        # Get div.subtitle
        main =  self.mysoup.find("div", {"id": "main"})
        if main == None:
            raise Exception("Missing div#main")
        
        table = fn_authortable.authortable(main)
        table.parseInfoTable()


        # Get div.pagedlbg
        pagedlbg =  self.mysoup.find("div", {"class": "pagedlbg"})
        if pagedlbg == None:
            raise Exception("Missing div.pagedlbg")
        
        #print(pagedlbg)
        contentarea = fn_contentarea.contentarea(pagedlbg)

        # Get the download element.
        downloadJsElement = pagedlbg.find("div", {"id": "hasJavaScript"})
        if downloadJsElement == None:
            raise Exception("Missing div#hasJavaScript")
        
        download = fn_downloaddetails.downloaddetails(downloadJsElement)
        
        try:
            download.parseElement()
        except Exception as e:
            #print(self.mysoup)
            print(e)
            print("section: "+ self.layoutparser.armaholicSection)
            time.sleep(5)
            #exit()
        
        contentarea.parse()
        
        #exit()

    def layout_1(self):
        print("layout_1")
        



        # Get div.subtitle
        subtitle =  self.mysoup.find("div", {"id": "subtitle"})
        if subtitle == None:
            raise Exception("Missing div#subtitle")
        
        table = fn_authortable.authortable(subtitle)
        table.parseInfoTable()
        


        # Get div.pagedlbg
        pagedlbg =  self.mysoup.find("div", {"class": "pagedlbg"})
        if pagedlbg == None:
            raise Exception("Missing div.pagedlbg")
        contentarea = fn_contentarea.contentarea(pagedlbg)
        

        # Get the download element.
        downloadJsElement = pagedlbg.find("div", {"id": "hasJavaScript"})
        if downloadJsElement == None:
            raise Exception("Missing div#hasJavaScript")
        
        download = fn_downloaddetails.downloaddetails(downloadJsElement)
        
        try:
            download.parseElement()
        except Exception as e:
            print(e)
            #print(self.mysoup)
            print("section: "+ self.layoutparser.armaholicSection)
            if self.layoutparser.armaholicSection == "arma_files_editing_scripts":
                time.sleep(1)
                pass
            elif self.layoutparser.armaholicSection =="arma_files_editing_tools":
                time.sleep(1)
                pass
            elif self.layoutparser.armaholicSection =="arma_files_editing_references":
                time.sleep(1)
                pass
            elif self.layoutparser.armaholicSection =="arma2_files_editing_scripts":
                time.sleep(1)
                pass
            elif self.layoutparser.armaholicSection =="arma2_oa_files_editing_tools":
                time.sleep(1)
                pass
            elif self.layoutparser.armaholicSecttion == "arma2_files_editing_templates":
                time.sleep(1)
                pass
            else:
                time.sleep(60)
                pass

        contentarea.parse()
        #print(self.mysoup)

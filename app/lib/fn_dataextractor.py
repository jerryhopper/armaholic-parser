from lib import fn_authortable
from lib import fn_downloaddetails
from lib import fn_contentarea

class extractor:
    debug=1
    content=False
    page_title_element=None
    foundLayout=False
    


    def x__str__(self) -> str:
        
        return  "---------pageparser.parser()\n"\
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
            raise Exception("NO RESULT FROM LAYOUTPARSER!")
        
        self.layoutparser = layoutparser
        self.mysoup = layoutparser.result
        
    
    def extract(self):
        # call the specific layout function.
        do = f"layout_{self.layoutparser.foundLayout}"
        
        # this will call function self.layout_?()
        if hasattr(self, do) and callable(getattr(self, do)):
            func = getattr(self, do)
            func()


    def layout_1(self):
        print("layout_1")
        

        
        # Do some cleaning.

        # remove div.footer
        x = self.mysoup.find("div", {"class": ["footer"]})
        x.extract()

        # remove div.footer
        x = self.mysoup.find("div", {"class": ["pageText"]})
        x.extract()

        # remove div.footer
        x = self.mysoup.find("div", {"class": ["rating"]})
        x.extract()
        
        # remove div#noscript
        x = self.mysoup.find("div", {"id": "noscript"})
        x.extract()

        # remove div#user
        x = self.mysoup.find("div", {"id": "user"})
        x.extract()

        # remove div#user
        x = self.mysoup.find("div", {"id": "nav"})
        x.extract()





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
        download.parseElement()

        #print(self.mysoup)



class contentarea:

    def __init__(self,soup):
        self.soup = soup
    
    def __str__(self) -> str:
        
        return  "---------fn_contentarea.py contentarea(soup)\n"\
                #"page_is_valid="+str(self.page_is_valid) +"\n"\
                #"page_template="+str(self.page_template) +"\n"\
                #"armaholicSection="+str(self.armaholicSection) +"\n"\
                #"page_html_title="+str(self.page_head_title) +"\n"\
                #"\n"

        #pass

    def cleanup(self):
        # Do some cleaning.

        # remove div#hasJavaScript
        self.soup.find("div", {"id": "hasJavaScript"}).extract()
        self.cleanEmptyPtags()
    
    def cleanEmptyPtags(self):
        # Iterate over each line of the document and extract the data
        for x in self.soup.find_all("p"):
            if len(x.get_text(strip=True)) == 0:
                x.extract()

    def parse(self):
        print("ContentArea!")
        #self.cleanup()

        #x= self.soup.find("div", {"class": ["pagedlbg"]})
        #print(x)
        #exit()
        # get links from content.
        
        # get images from content

        # get videos from content

        # check if 'requirements' are detected.
        # find:
        # <img src="/web/20171027011429im_/http://www.armaholic.com/skins/Blaster07/img/required_addons.png" alt="">
        #  
        # 
        # 
        # 

        # finally get the html
        #print(self.soup)
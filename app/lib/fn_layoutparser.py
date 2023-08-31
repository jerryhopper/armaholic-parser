import os,sys,time

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class parser:
    debug=1
    content=False
    page_title_element=None
    foundLayout=False
    
    def __str__(self) -> str:
        
        return  "---------pageparser.parser()\n"\
                #"page_is_valid="+str(self.page_is_valid) +"\n"\
                #"page_template="+str(self.page_template) +"\n"\
                #"armaholicSection="+str(self.armaholicSection) +"\n"\
                #"page_html_title="+str(self.page_head_title) +"\n"\
                #"\n"

        #pass

    def remove_script_tags(self):
        [s.extract() for s in self.soup('script')]

    def remove_center_tags(self):
        [s.extract() for s in self.soup('center')]

    def getChildWithId(self, element, tag, id):
        for el in element.find_all(recursive=False):
            if el.name == tag:
                try:
                    if el['id'] == id:
                        return el
                except Exception as e:
                    pass
        raise Exception("No element '"+tag+"' found where id="+id)

    def getChildWithClass(self, element, tag, classname):
        for el in element.find_all(recursive=False):
            if el.name == tag:
                try:
                    if classname in el['class']:
                        return el
                except Exception as e:
                    pass
        raise Exception("No element '"+tag+"' found where class="+classname)
    
    def getChildWithTag(self,element,tag):
        for el in element.find_all(recursive=False):
            if el.name == tag:
                return el
        raise Exception("No element '"+tag+"' found ")


    def elementPropertyHelper(self,element):
        line = element.name+" "
        try:
            line = line +" id='"+element['id']+"'"
            #print(j.name+" id="+j['id'])
        except Exception as e:
            pass
        try:
            line = line +" class='"
            for c in element['class']:
                line = line + c +" "
            #print(j.name+" class="+j['class'])
            line = line + " ' "
        except Exception as e:
            pass
        return line+"'>"


    def listChildrenHelper(self,element):
        #print("\n-listChildrenHelper----- <"+self.elementPropertyHelper(element) )
        childList = []
        for j in element.find_all(recursive=False):
            line = ""+j.name+""
            try:
                line = line +"#"+j['id']+""
                #print(j.name+" id="+j['id'])
            except Exception as e:
                a=1
            try:
                #line = line 
                for c in j['class']:
                    line = line + "."+ c +""
                #print(j.name+" class="+j['class'])
                line = line + ""
            except Exception as e:
                a=1
            line = line + ""
            childList.append(line.strip())
            #print(line.strip())
        return childList
    
    
        


    def layout1(self,body):
        #
        # body div.wrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div.wrap")
            #print(body)
            #exit()


        x = self.listChildrenHelper(wrap)
                  
        if x[0]!='div#container':
            raise Exception("0 != div#container")    
        
        if x[1]!='div#title':
            raise Exception("1 != div#title")    
        
        if x[2]!='div#subtitle':
            raise Exception("2 != div#subtitle")    
        
        if x[3]!='div.pagedlbg':
            raise Exception("3 != div#pagedlbg")    
        
        if x[4]!='hr':
            raise Exception("5 != hr")   
        
        if x[5]!='div#main':
            raise Exception("6 != div#main")         
        
        if x[6]!='div.footer':
            raise Exception("7 != div.footer") 
        
        #print(wrap)
        #exit()
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = wrap.find(id="title")
        #print(self.page_title_element)
        #exit()

        return wrap
        
    def layout2(self,body):
        
        
        x = self.listChildrenHelper(body)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div#title':
            raise Exception("1 != div#title")

        if x[2]!='div#subtitle':
            raise Exception("2 != div#subtitle")
        
        if x[3]!='div.pagedlbg':
            raise Exception("3 != div.pagedlbg")    

        if x[4]!='table':
            raise Exception("4 != table")    
        
        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)
        if x[6]!='div.footer':
            raise Exception("6 != div.footer")    
            print(x)
        
        #print("layout2")
        #print(x)
        #self.page_title_element=0
        #self.armaholicSection="_newsarma_"
        self.page_title_element = body.find(id="title")
        #print(wrap)
        #exit()
        return body
        
    def layout3(self,body):
        
        
        x = self.listChildrenHelper(body)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div#title':
            raise Exception("1 != div#title")

        if x[2]!='div#main':
            raise Exception("2 != div#main")    
            print(x)
        
        if x[3]!='div.pagedlbg':
            raise Exception("3 != div.pagedlbg")    

        if x[4]!='hr':
            raise Exception("4 != hr")    

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='div.footer':
            raise Exception("6 != div.footer")    
            print(x)
        
        print("layout3")
        #print(x)


    def layout4(self,body):
        #
        # body div.wrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div.wrap")
            #print(body)
            #exit()  
            #      
        x = self.listChildrenHelper(wrap)
        #print(x)
        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div#title':
            raise Exception("1 != div#title")

        if x[2]!='div#main':
            raise Exception("2 != div#main")    
            print(x)
        
        if x[3]!='div.pagedlbg':
            raise Exception("3 != div.pagedlbg")    

        if x[4]!='hr':
            raise Exception("4 != hr")    

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='div.footer':
            raise Exception("6 != div.footer")    
            print(x)

        #print(wrap)
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = wrap.find(id="title")
        #print(self.page_title_element)
        #exit()
        #raise Exception("fin")   
        return wrap
    

    def layout5(self,body):
        #
        # body div.wrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div.wrap")
            #print(body)
            #exit()  
            #      
        x = self.listChildrenHelper(wrap)
        
        #print(x)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div#title':
            raise Exception("1 != div#title")

        if x[2]!='div#subtitle':
            raise Exception("2 != div#subtitle")    
            print(x)
        
        if x[3]!='div.pagedlbg':
            raise Exception("3 != div.pagedlbg")    

        if x[4]!='table':
            raise Exception("4 != table")    

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='div.footer':
            raise Exception("6 != div.footer")    
            print(x)

        #print(wrap)
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = body.find(id="title")
        #
        #raise Exception("fin")   
        return wrap


    def layout6(self,body):
        #
        # body div.wrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div.wrap")
            #print(body)
            #exit()  
            #      
        x = self.listChildrenHelper(wrap)
        
        #print(x)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div#title':
            raise Exception("1 != div#title")

        if x[2]!='div#main':
            raise Exception("2 != div#main")    
            print(x)
        
        if x[3]!='div.pagedlbg':
            raise Exception("3 != div.pagedlbg")    

        if x[4]!='table':
            raise Exception("4 != table")    

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='div.footer':
            raise Exception("6 != div.footer")    
            print(x)

        #self.page_title_element=0
        #self.armaholicSection="_newsarma_"
        self.page_title_element = wrap.find(id="title")
        #print(wrap)
        #exit()
        return wrap
        #raise Exception("fin")   



    def layout7(self,body):
        #
        # body div.wrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div.wrap")
            #print(body)
            #exit()  
            #      
        x = self.listChildrenHelper(wrap)
        
        #print(x)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div':
            raise Exception("1 != div")

        if x[2]!='br':
            raise Exception("2 != br")    
            print(x)
        
        if x[3]!='div#title':
            raise Exception("3 != div#title")    

        if x[4]!='div#subtitle':
            raise Exception("4 != div#subtitle")    

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='table.download':
            raise Exception("6 != table.download")    
            print(x)

        if x[7]!='br':
            raise Exception("7 != br")    
            print(x)

        if x[8]!='br':
            raise Exception("8 != br")    
            print(x)

        if x[9]!='strong':
            raise Exception("9 != strong")    
            print(x)

        if x[10]!='br':
            raise Exception("10 != br")    
            print(x)

        if x[11]!='table':
            raise Exception("11 != table")    
            print(x)

        if x[12]!='div.footer':
            raise Exception("12 != div.footer")    
            print(x)


        #raise Exception("fin")   

    def layout8(self,body):
        #
        # body div.wrap 
        #
        #try:
        #    wrap = self.getChildWithId( body, 'div', 'wrap')
        #    #self.listChildrenHelper(wrap)
        #except Exception as e:
        #    raise Exception("No div.wrap")
        #    #print(body)
        #    #exit()  
        #    #      
        x = self.listChildrenHelper(body)
        
        #print(x)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
                
        if x[1]!='div':
            raise Exception("1 != div")

        if x[2]!='br':
            raise Exception("2 != br")    
            print(x)
        
        if x[3]!='div#title':
            raise Exception("3 != div#title")    

        if x[4]!='div#subtitle':
            raise Exception("4 != div#subtitle")    

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='table.download':
            raise Exception("6 != table.download")    
            print(x)

        if x[7]!='br':
            raise Exception("7 != br")    
            print(x)

        if x[8]!='br':
            raise Exception("8 != br")    
            print(x)

        if x[9]!='strong':
            raise Exception("9 != strong")    
            print(x)

        if x[10]!='br':
            raise Exception("10 != br")    
            print(x)

        if x[11]!='table':
            raise Exception("11 != table")    
            print(x)

        if x[12]!='div.footer':
            raise Exception("12 != div.footer")    
            print(x)

        #print(wrap)
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = body.find(id="title")
        #

        return body
        #raise Exception("fin")   

    def layout9(self,body):
        x = self.listChildrenHelper(body)
        
        #print(x)

        if x[0]!='div#container':
            raise Exception("0 != div#container")    
        
        if x[1]!='div#title':
            raise Exception("1 != div#title")    

        if x[2]!='div#main':
            raise Exception("2 != div#main")    
            print(x)

        if x[3]!='div.pagedlbg':
            raise Exception("3 != div.pagedlbg")    
            print(x)

        if x[4]!='table':
            raise Exception("4 != table")    
            print(x)

        if x[5]!='div#main':
            raise Exception("5 != div#main")    
            print(x)

        if x[6]!='div.footer':
            raise Exception("6 != div.footer")    
            print(x)

        self.page_title_element = body.find(id="title")
        #raise Exception("fin")   



    def layout10(self,body):

        #
        # body div.bigwrap 
        #
        try:
            bigwrap = self.getChildWithId( body, 'div', 'bigwrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#bigwrap")
            #print(body)
            #exit()  
            #  

        #x = self.listChildrenHelper(body)
        
        #print(x)


        x = self.listChildrenHelper(bigwrap)
        
        #print(x)

        if x[0]!='img':
            raise Exception("0 != img")    
        
        if x[1]!='map':
            raise Exception("1 != map")    

        if x[2]!='div#wrap':
            raise Exception("2 != div#wrap")    
            print(x)

        #self.page_title_element = body.find(id="title")




        wrap = self.getChildWithId( bigwrap, 'div', 'wrap')

        y = self.listChildrenHelper(wrap)
        #print(y)
        


        if y[0]!='div#container':
            raise Exception("0 != div#container")    
        
        if y[1]!='div#middlecontainer':
            raise Exception("1 != div#middlecontainer")    

        if y[2]!='div#container2':
            raise Exception("2 != div#container2")    
            print(x)

        if y[3]!='div#title':
            raise Exception("3 != div#title")    
            print(x)
        
        self.page_title_element = body.find(id="title")

        if y[4]!='div#subtitle':
            raise Exception("4 != div#subtitle")    
            print(x)


        if y[5]!='div.pagedlbg':
            raise Exception("5 != div.pagedlbg")    
            print(x)


        if y[6]!='table':
            raise Exception("6 != table")    
            print(x)


        if y[7]!='div#main':
            raise Exception("7 != div#main")    
            print(x)

        if y[8]!='div.footer':
            raise Exception("8 != div.footer")    
            print(x)

        #print(x)

        #raise Exception("fin")   




    def layout11(self,body):

        #
        # body div.bigwrap 
        #
        try:
            bigwrap = self.getChildWithId( body, 'div', 'bigwrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#bigwrap")
            #print(body)
            #exit()  
            #  

        #x = self.listChildrenHelper(body)
        
        #print(x)


        x = self.listChildrenHelper(bigwrap)
        
        #print(x)

        if x[0]!='img':
            raise Exception("0 != img")    
        
        if x[1]!='map':
            raise Exception("1 != map")    

        if x[2]!='div#wrap':
            raise Exception("2 != div#wrap")    
            print(x)




        wrap = self.getChildWithId( bigwrap, 'div', 'wrap')

        y = self.listChildrenHelper(wrap)
        #print(y)
        
        if y[0]!='div#container':
            raise Exception("0 != div#container")    
        
        if y[1]!='div#middlecontainer':
            raise Exception("1 != div#middlecontainer")    

        if y[2]!='div#container2':
            raise Exception("2 != div#container2")    
            print(x)

        if y[3]!='div#title':
            raise Exception("3 != div#title")    
            print(x)

        if y[4]!='div#main':
            raise Exception("4 != div#main")    
            print(x)


        if y[5]!='div.pagedlbg':
            raise Exception("5 != div.pagedlbg")    
            print(x)


        if y[6]!='table':
            raise Exception("6 != table")    
            print(x)


        if y[7]!='div#main':
            raise Exception("7 != div#main")    
            print(x)

        if y[8]!='div.footer':
            raise Exception("8 != div.footer")    
            print(x)

        #print(x)
        self.page_title_element = wrap.find(id="title")
        #raise Exception("fin")   


    def layout12(self,body):


        x = self.listChildrenHelper(body)
        
        if x[0]!="div#wrap":
            raise Exception("0 != div#wrap")
        if x[1]!="hr":
            raise Exception("1 != hr")
        if x[2]!="div#main":
            raise Exception("2 != div#main")
        if x[3]!="div.footer":
            raise Exception("3 != div.footer")



        # body div.bigwrap 
        #
        try:
            bigwrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
            #print(body)
            #exit()  
            #  

        

        x = self.listChildrenHelper(bigwrap)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div#title":
            raise Exception("1 != div#title")
        if x[2]!="div#main":
            raise Exception("2 != div#main")
        if x[3]!="div.pagedlbg":
            raise Exception("3 != div.pagedlbg")
        if x[4]!="br":
            raise Exception("4 != br")
        
        self.page_title_element = bigwrap.find(id="title")

        #




    def layout13(self,body):


        x = self.listChildrenHelper(body)
        
        if x[0]!="div#wrap":
            raise Exception("0 != div#wrap")
        if x[1]!="div#main":
            raise Exception("2 != div#main")
        if x[2]!="div.footer":
            raise Exception("3 != div.footer")



        # body div.bigwrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
            #print(body)
            #exit()  
            #  
        self.page_title_element = wrap.find(id="title")
        #x = self.listChildrenHelper(wrap)
        #print(x)
        #exit("+++++++++++++++++++++++")

    def layout14(self,body):


        x = self.listChildrenHelper(body)
        
        if x[0]!="div#wrap":
            raise Exception("0 != div#wrap")
        if x[1]!="br":
            raise Exception("1 != br")
        if x[2]!="br":
            raise Exception("2 != br")
        if x[3]!="div.footer":
            raise Exception("3 != div.footer")



        # body div.bigwrap 
        #
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
            #print(body)
            #exit()  
            #  

        x = self.listChildrenHelper(wrap)
        #print(x)
        if x[0]!="div#container":
            raise Exception("0 != div#wrap")
        if x[1]!="br":
            raise Exception("1 != br")
        if x[2]!="div":
            raise Exception("2 != div")
        if x[3]!="br":
            raise Exception("3 != br")
        if x[4]!="div#title":
            raise Exception("4 != div#title")
        if x[5]!="div#subtitle":
            raise Exception("5 != div#subtitle")
        if x[6]!="div#main":
            raise Exception("6 != div#main")
        if x[7]!="div.block":
            raise Exception("7 != div.block")
        if x[8]!="div.download":
            raise Exception("8 != div.download")
        
        self.page_title_element = wrap.find(id="title")

        #exit("+++++++++++++++++++++++")
        


    def layout15(self,body):

        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            
        except Exception as e:
            raise Exception("No div#wrap")


        x = self.listChildrenHelper(wrap)
        #print(x)
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div.news_ad":
            raise Exception("1 != div.news_ad")
        if x[2]!="table":
            raise Exception("2 != table")


        self.page_title_element = wrap.find(id="fondonews")
        #print(self.page_title_element)
        #exit()
        return wrap

    

    def layout16(self,body):
        #print("L16")
        #x = self.listChildrenHelper(body)
        #print(x)

        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
        
        x = self.listChildrenHelper(wrap)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div#title":
            raise Exception("1 != div#title")
        if x[2]!="div#subtitle":
            raise Exception("2 != div#subtitle")
        if x[3]!="div.pagedlbg":
            raise Exception("3 != div.pagedlbg")
        

        self.page_title_element = wrap.find(id="title")
        #print(self.page_title_element)

        return wrap        
        #exit()

    def layout17(self,body):
        #print("L16")
        #x = self.listChildrenHelper(body)
        #print(x)

        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
        
        x = self.listChildrenHelper(wrap)
        #print(x)
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div#subtitle":
            raise Exception("1 != div#subtitle")
        if x[2]!="div#main":
            raise Exception("2 != div#main")
        if x[3]!="div.footer":
            raise Exception("3 != div.footer")
        
        #print(wrap)
        self.page_title_element=0
        self.armaholicSection="_site_pages"
        #self.page_title_element = wrap.find(id="fondonews")
        #print(self.page_title_element)
        #exit()


    def layout18(self,body):
        #print("L16")
        #x = self.listChildrenHelper(body)
        #print(x)

        try:
            wrap = self.getChildWithId( body, 'div', 'container')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
        
        x = self.listChildrenHelper(wrap)
        #print(x)
        if x[0]!="div#hd_left":
            raise Exception("0 != div#hd_left")
        if x[1]!="div#banner":
            raise Exception("1 != div#banner")
        if x[2]!="div#hd_right":
            raise Exception("2 != div#hd_right")
        if x[3]!="div#nav_left":
            raise Exception("3 != div#nav_left")
        if x[4]!="div#nav":
            raise Exception("4 != div#nav")
        #print(wrap)
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = wrap.find(id="title")
        #print(self.page_title_element)
        #exit()


    def layout19(self,body):
        #print("L16")
        x = self.listChildrenHelper(body)
        #print(x)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div":
            raise Exception("1 != div")
        if x[2]!="br":
            raise Exception("2 != br")
        if x[3]!="div#title":
            raise Exception("3 != div#title")
        if x[4]!="div#subtitle":
            raise Exception("4 != div#subtitle")
        if x[5]!="div#main":
            raise Exception("5 != div#main")
        if x[6]!="table.download":
            raise Exception("4 != table.download")

        #print(wrap)
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = wrap.find(id="title")
        #print(self.page_title_element)
        #exit()
        #raise Exception("fin")  
        return body

    def layout20(self,body):
        #print("L16")
        x = self.listChildrenHelper(body)
        #print(x)
        
        if x[0]!="div#dialog-mask.page-loader":
            raise Exception("0 != div#dialog-mask.page-loader")
        if x[1]!="div.header":
            raise Exception("1 != div.header")
        if x[2]!="div.navbar.futuristic":
            raise Exception("2 != div.navbar.futuristic")

        #print(body)
        #exit()
        self.page_title_element=0
        self.armaholicSection="_casino_pages"
        #self.page_title_element = body.find(id="title")
        #

        return body
    
    def layout21(self,body):
        
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
        
        x = self.listChildrenHelper(wrap)
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="table":
            raise Exception("1 != table")
        if x[2]!="div.footer":
            raise Exception("2 != div.footer")
        #print(x)
        #exit()
        #exit()
        self.page_title_element=0
        self.armaholicSection="_newsarma_"
        #self.page_title_element = body.find(id="title")
        #print(wrap)
        #exit()
        return wrap
    
    def layout22(self,body):
        
        #try:
        #    wrap = self.getChildWithId( body, 'div', 'wrap')
        #    #self.listChildrenHelper(wrap)
        #except Exception as e:
        #    raise Exception("No div#wrap")
        
        x = self.listChildrenHelper(body)
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="br":
            raise Exception("1 != br")
        if x[2]!="div":
            raise Exception("2 != div")
        if x[3]!="br":
            raise Exception("3 != br")
        if x[4]!="div.cobo_dark":
            raise Exception("4 != div.cobo_dark")
        #print(x)
        #exit()
        #self.page_title_element=0
        #self.armaholicSection="_newsarma_"
        self.page_title_element = body.find(id="title")
        #print(body)
        #exit()
        return body


    def layout23(self,body):
        
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
        


        x = self.listChildrenHelper(wrap)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="table":
            raise Exception("1 != table")
        
        #print(body)

        self.page_title_element = body.find(id="fondonews")

        return wrap

    def layout24(self,body):
        
        x = self.listChildrenHelper(body)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div":
            raise Exception("1 != div")
        if x[2]!="br":
            raise Exception("2 != br")
        if x[3]!="div#title":
            raise Exception("3 != div#title")
        if x[4]!="div#subtitle":
            raise Exception("4 != div#subtitle")
        if x[5]!="div#main":
            raise Exception("5 != div#main")        
        if x[6]!="br":
            raise Exception("6 != br")   
        if x[7]!="div.footer":
            raise Exception("6 != div.footer")

        #if x[2]!="div":
        #    raise Exception("2 != div")
        #if x[3]!="br":
        #    raise Exception("3 != br")
        #if x[4]!="div.cobo_dark":
        #    raise Exception("4 != div.cobo_dark")
        #print(x)
        #exit()
        self.page_title_element = body.find(id="title")



    def layout25(self,body):
        
        try:
            wrap = self.getChildWithId( body, 'div', 'wrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")
        
        x = self.listChildrenHelper(wrap)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div#title":
            raise Exception("1 != div#title")
        if x[2]!="div#main":
            raise Exception("2 != div#main")
        if x[3]!="div.footer":
            raise Exception("3 != div.footer")
        #print(x)
        #exit()
        self.page_title_element = wrap.find(id="title")

    def layout26(self,body):
        
        
        
        x = self.listChildrenHelper(body)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div":
            raise Exception("1 != div")
        if x[2]!="div.footer":
            raise Exception("2 != div.footer")
        
        #x= body.find(id="container")
        #print(x)
        #exit()
        #print(wrap)
        self.page_title_element=0
        self.armaholicSection="_site_pages_accessdenied"
        #self.page_title_element = body.find(id="title")
        #print(self.page_title_element)


    def layout27(self,body):
        
        x = self.listChildrenHelper(body)
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="table":
            raise Exception("1 != table")
        if x[2]!="div.footer":
            raise Exception("2 != div.footer")
        #print(x)

        table = self.getChildWithTag(body,"table")

        #print(table)
        #x = self.listChildrenHelper(table)
        #print(x)
        

        self.page_title_element = table.find(id="fondonews")

        

    def layout28(self,body):
        
        try:
            wrap = self.getChildWithId( body, 'div', 'bigwrap')
            #self.listChildrenHelper(wrap)
        except Exception as e:
            raise Exception("No div#wrap")

        x = self.listChildrenHelper(wrap)
        #print(x)
        #exit()
        if x[0]!="img":
            raise Exception("0 != img")
        if x[1]!="map":
            raise Exception("1 != map")
        if x[2]!="div#wrap":
            raise Exception("2 != div#wrap")
        
        wrap = self.getChildWithId( wrap, 'div', 'wrap')
        x = self.listChildrenHelper(wrap)

        #print(x)
        #print(wrap)

        ## this one sometimes has title, or fondonews as sectionlist.
        ## on armaholicid: 9935 its stuck coz no 'title'
        self.page_title_element = wrap.find(id="title")
        ## on armaholicid: its stuck coz no 'fondonews' 
        #self.page_title_element = body.find(id="fondonews")

        check = wrap.find(id="title")
        if check == None:
            check = body.find(id="fondonews")
        
        if check == None:
            self.page_title_element = check
        else:
            raise Exception("Layout28 error!")



    def layout29(self,body):


        x = self.listChildrenHelper(body)
        #print(x)
        #exit()
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div#title":
            raise Exception("1 != div#title")
        if x[2]!="div#subtitle":
            raise Exception("2 != div#subtitle")
        if x[3]!="div#main":
            raise Exception("3 != div#main")
        if x[4]!="table.download":
            raise Exception("4 != table.download")
        if x[5]!="br":
            raise Exception("5 != br")
        if x[6]!="strong":
            raise Exception("6 != strong")
        self.page_title_element = body.find(id="title")
        #print(x)
        #exit()


    def layout30(self,body):
        x = self.listChildrenHelper(body)
        #print(x)
        #exit()
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div#title":
            raise Exception("1 != div#title")
        if x[2]!="div#subtitle":
            raise Exception("2 != div#subtitle")

        if x[3]!="table":
            raise Exception("3 != table")
        if x[4]!="div#main":
            raise Exception("4 != div#main")
        if x[5]!="div.footer":
            raise Exception("5 != div.footer")       
        #print(x)
        #exit()
        self.page_title_element = body.find(id="title")


    def layout31(self,body):
        x = self.listChildrenHelper(body)
        
        if x[0]!="div#wrap":
            raise Exception("0 != div#wrap")
        if x[1]!="td#right_col":
            raise Exception("1 != td#right_col")
        if x[2]!="tr":
            raise Exception("2 != tr")
        if x[3]!="div.footer":
            raise Exception("3 != div.footer")
        #print(body)
        #exit()
        self.page_title_element = body.find(id="fondonews")

    def layout32(self,body):
        x = self.listChildrenHelper(body)
        
        if x[0]!="amp-analytics":
            raise Exception("0 != amp-analytics")
        if x[1]!="input#DeviceToken.JSBridge":
            raise Exception("1 != input#DeviceToken.JSBridge")
        if x[2]!="input#DeviceID.JSBridge":
            raise Exception("2 != input#DeviceID.JSBridge")
        if x[3]!="div.wrapper":
            raise Exception("3 != div.wrapper")
        #print(x)
        #exit()
        self.page_title_element=0
        self.armaholicSection="casino_pages"
        #self.page_title_element = body.find(id="title")


    def layout33(self,body):
        x = self.listChildrenHelper(body)
        
        #print(x)
        #exit()

        if x[0]!="div#wrap":
            raise Exception("0 != div#wrap")
        if x[1]!="div#main":
            raise Exception("1 != div#main")
        if x[2]!="br":
            raise Exception("2 != br")
        if x[3]!="br":
            raise Exception("3 != br")
        if x[4]!="div#fondonews":
            raise Exception("4 != div#fondonews")
        if x[5]!="hr":
            raise Exception("5 != hr")
        if x[6]!="div.footer":
            raise Exception("6 != div.footer")
        
        #self.page_title_element=0
        #self.armaholicSection="casino_pages"
        self.page_title_element = body.find(id="title")
        #print(body.find(id="title"))
        #exit()

    def layout34(self,body):
        x = self.listChildrenHelper(body)
        
        
        if x[0]!="div#container":
            raise Exception("0 != div#container")
        if x[1]!="div":
            raise Exception("1 != div")
        if x[2]!="br":
            raise Exception("2 != br")
        if x[3]!="div#title":
            raise Exception("3 != div#title")
        if x[4]!="div#subtitle":
            raise Exception("4 != div#subtitle")
        if x[5]!="div#main":
            raise Exception("5 != div#main")
        if x[6]!="table.download":
            raise Exception("6 != table.download")
        if x[7]!="br":
            raise Exception("6 != br")
        #if x[8]!="strong":
        #    raise Exception("6 != strong")
        
        #print(wrap)
        #self.page_title_element=0
        #self.armaholicSection="_site_pages"
        self.page_title_element = body.find(id="title")
        #print(self.page_title_element)
        #exit()
        
        return body
        
    
    def layout35(self,body):
        x = self.listChildrenHelper(body)
        
        
        if x[0]!="div#bigwrap":
            raise Exception("0 != div#bigwrap")
        if x[1]!="tr":
            raise Exception("1 != tr")
        if x[2]!="div.footer":
            raise Exception("2 != div.footer")
    
        self.page_title_element = body.find(id="fondonews")
        #print(self.page_title_element)
        #print(body)
        #exit("-=Fin=-")


    def layout36(self,body):
        x = self.listChildrenHelper(body)
        
        #print(body)
        if x[0]!="div#bigwrap":
            raise Exception("0 != div#bigwrap")
        
        if "Access denied" in body.find(id="title").text:
            #print( "ohh" )
            self.page_title_element=0
            self.armaholicSection="_site_pages_accessdenied"

        #exit()
        #if x[1]!="tr":
        #    raise Exception("1 != tr")
        #if x[2]!="div.footer":
        #    raise Exception("2 != div.footer")
        
        
        #self.page_title_element = body.find(id="fondonews")
        #print(self.page_title_element)
        #print(body)
        #exit("-=Fin=-")





























    def __init__(self,soup):
        self.soup = soup

        self.remove_script_tags()
        self.remove_center_tags()


        try:
            self.page_head_title = self.soup.find("title").text.strip()
        except Exception as e:
            print("No Header?")
            pass

        
        body = self.soup.find("body")
        if body == None:
            
            raise Exception ("NO BODY TAG!")














        self.foundLayout=False

        try:
            if self.foundLayout == False:
                self.result = self.layout1(body)
                self.foundLayout=1
                
                #print(self.armaholicSection)
                #print(result)
                #exit(1)
        except Exception as e:
            #print(body)
            #print(e)
            #self.listChildrenHelper(body)
            #print("Not layout 1")
            #exit()
            pass

        try:
            if self.foundLayout == False:
                self.layout2(body)
                self.foundLayout=2
        except Exception as e:
            #print(e)
            #print("Not layout 2")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout3(body)
                self.foundLayout=3
        except Exception as e:
            #print(e)
            #print("Not layout 3")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout4(body)
                self.foundLayout=4
        except Exception as e:
            #print(e)
            #print("Not layout 4")
            pass
            #print(body)
            #exit()
        
        try:
            if self.foundLayout == False:
                self.layout5(body)
                self.foundLayout=5
        except Exception as e:
            #print(e)
            #print("Not layout 5")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout6(body)
                self.foundLayout=6
        except Exception as e:
            #print(e)
            #print("Not layout 6")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout7(body)
                self.foundLayout=7
        except Exception as e:
            #print(e)
            #print("Not layout 7")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout8(body)
                self.foundLayout=8
                
        except Exception as e:
            #print(e)
            #print("Not layout 8")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout9(body)
                self.foundLayout=9
                
        except Exception as e:
            #print(e)
            #print("Not layout 9")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout10(body)
                self.foundLayout=10
                
        except Exception as e:
            #print(e)
            #print("Not layout 10")
            pass
            #print(body)
            #exit()


        try:
            if self.foundLayout == False:
                self.layout11(body)
                self.foundLayout=11
                
        except Exception as e:
            #print(e)
            #print("Not layout 11")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout12(body)
                self.foundLayout=12
                
        except Exception as e:
            #print(e)
            #print("Not layout 12")
            pass
            #print(body)
            #exit()



        try:
            if self.foundLayout == False:
                self.layout13(body)
                self.foundLayout=13
                
        except Exception as e:
            #print(e)
            #print("Not layout 13")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout14(body)
                self.foundLayout=14
                
        except Exception as e:
            #print(e)
            #print("Not layout 14")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout15(body)
                self.foundLayout=15
                
        except Exception as e:
            #print(e)
            #print("Not layout 15")
            pass
            #print(body)
            #exit()

        try:
            if self.foundLayout == False:
                self.layout16(body)
                self.foundLayout=16
                
        except Exception as e:
            #print(e)
            #print("Not layout 16")
            pass


        try:
            if self.foundLayout == False:
                self.layout17(body)
                self.foundLayout=17
        except Exception as e:
            #print(e)
            #print("Not layout 17")
            pass


        try:
            if self.foundLayout == False:
                self.layout18(body)
                self.foundLayout=18
                
        except Exception as e:
            #print(e)
            #print("Not layout 18")
            pass

        try:
            if self.foundLayout == False:
                self.layout19(body)
                self.foundLayout=19
                
        except Exception as e:
            #print(e)
            #print("Not layout 19")
            pass


        try:
            if self.foundLayout == False:
                self.layout20(body)
                self.foundLayout=20
                
        except Exception as e:
            #print(e)
            #print("Not layout 20")
            pass

        try:
            if self.foundLayout == False:
                self.layout21(body)
                self.foundLayout=21
                
        except Exception as e:
            #print(e)
            #print("Not layout 21")
            pass

        try:
            if self.foundLayout == False:
                self.layout22(body)
                self.foundLayout=22
                
        except Exception as e:
            #print(e)
            #print("Not layout 22")
            pass


        try:
            if self.foundLayout == False:
                self.layout23(body)
                self.foundLayout=23
                
        except Exception as e:
            #print(e)
            #print("Not layout 23")
            pass


        try:
            if self.foundLayout == False:
                self.layout24(body)
                self.foundLayout=24
                
        except Exception as e:
            #print(e)
            #print("Not layout 24")
            pass

        try:
            if self.foundLayout == False:
                self.layout25(body)
                self.foundLayout=25
                
        except Exception as e:
            #print(e)
            #print("Not layout 25")
            pass

        try:
            if self.foundLayout == False:
                self.layout26(body)
                self.foundLayout=26
                
        except Exception as e:
            #print(e)
            #print("Not layout 26")
            pass

        try:
            if self.foundLayout == False:
                self.layout27(body)
                self.foundLayout=27
                
        except Exception as e:
            #print(e)
            #print("Not layout 27")        
            pass


        try:
            if self.foundLayout == False:
                self.layout28(body)
                self.foundLayout=28
                
        except Exception as e:
            #print(e)
            #print("Not layout 28")
            pass     

        try:
            if self.foundLayout == False:
                self.layout29(body)
                self.foundLayout=29
                
        except Exception as e:
            #print(e)
            #print("Not layout 29")
            pass

        try:
            if self.foundLayout == False:
                self.layout30(body)
                self.foundLayout=30
                
        except Exception as e:
            #print(e)
            #print("Not layout 30")
            pass

        try:
            if self.foundLayout == False:
                self.layout31(body)
                self.foundLayout=31
                
        except Exception as e:
            #print(e)
            #print("Not layout 31")
            pass



        try:
            if self.foundLayout == False:
                self.layout32(body)
                self.foundLayout=32
                
        except Exception as e:
            #print(e)
            #print("Not layout 32")
            pass

        try:
            if self.foundLayout == False:
                self.layout33(body)
                self.foundLayout=33
                
        except Exception as e:
            #print(e)
            #print("Not layout 33")
            pass

        try:
            if self.foundLayout == False:
                self.layout34(body)
                self.foundLayout=34
                
        except Exception as e:
            #print(e)
            #print("Not layout 34")
            pass

        try:
            if self.foundLayout == False:
                self.layout35(body)
                self.foundLayout=35
                
        except Exception as e:
            #print(e)
            #print("Not layout 35")
            pass

        try:
            if self.foundLayout == False:
                self.layout36(body)
                self.foundLayout=36
                
        except Exception as e:
            print(e)
            print("Not layout 36")






        if self.foundLayout == False:
            print("-------------------------")
            print("Unknown layout!")
            x = self.listChildrenHelper(body)
            print(x)
            exit(".........")
        else:
            self.getSection()
            #print("layout: "+str(self.foundLayout)+ " "+self.page_head_title )
            
        return
        exit()


        
        
        #self.findInfoTable()
        #print(soup)
        #exit()









    def getSection(self):
        #
        # Get Section and Armaholic ID from the breadcrumbs
        #
        try:
            titleresult = self.page_title_element #soup.find(id="title")
            
            #print(titleresult)
            #return
            title_links = titleresult.find_all("a", href=True)
            titleLinkList = []
            for link in title_links:
                titleLinkList.append(self.parseTitleLinkQueryString(link['href']))

            # store the results
            self.armaholicSection = titleLinkList[-2]
            self.armaholicId = int(titleLinkList[-1])
        except Exception as e:
            self.armaholicSection = "UNKNOWN"
            pass
        return self.armaholicSection

    def parseTitleLinkQueryString(self,value):
        parse_result = urlparse(value)
        dict_result = parse_qs(parse_result.query)
        try :
            return dict_result['c'][0]
        except Exception as e:
            return int(dict_result['id'][0])  

    def findInfoTable(self):
        #
        # Get the information-table
        #
        # the information table is always a 'table' which contains Author:
        #
        
        infoTable=None

        # check for -> wrap -> main -> <table>
        wrapper = self.soup.find(id="wrap")
        if wrapper != None:
            # check if main is a sub of wrapper
            main=wrapper.find(id="main")
            if wrapper != None:
                infoTable =main.find("table")
        else:
            container = self.soup.find(id="container")
            if container != None:
                infoTable =container.find("table")
            else:
                print(container)
                exit("NO div-container -> table")

        # check for -> subtitle -> <table>
        if infoTable==None:
            #subtitle
            print("WARNING! : Page layout different. infoTable is not found in 'main'. Checking 'subtitle'")
            main=wrapper.find(id="subtitle")
            
            print(main)
            infoTable =main.find("table")
            
            #print(infoTable)
        else :
            #print(infoTable)
            infoTable =infoTable
        
        #print(infoTable)
        #exit()
        try:
            self.parseInfoTable(infoTable)
        except Exception as e:
            print(infoTable)
            print(e)
            exit()


    def parseUserLinkQueryString(self,value):
        print("-> parseUserLinkQueryString")
        print(value)
        parse_result = urlparse(value)
        dict_result = parse_qs(parse_result.query)
        return dict_result['id'][0]


    def parseInfoTable(self,table):
        if self.debug == 1: print("parseInfoTable")
        div = table.find_all('div')

        #tds = div[0].find_all('font')

        lines = div[1].text.split("\n")
        for line in lines:
            if line != "":
                if "Date:" in line:
                    self.date =line.split(": ")[1][:16]
                    #16
                    print(self.date)
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
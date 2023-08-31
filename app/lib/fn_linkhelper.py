
from urllib.parse import urlparse, parse_qs

class linkhelper:
    
    wbpath = False
    originalUrl = False
    url = False

    def __init__(self):
        a=1
        #x = self.parseWayBackUrl(URL)
        #parts =x.path.split('/')
        #self.wbpath = "/"+parts[1]+"/"+parts[2]
        #exit()

    def parseUserLinkQueryString(self,value):
        if self.debug == 1: print("-> parseUserLinkQueryString")
        if self.debug == 1: print(value)
        parse_result = urlparse(value)
        dict_result = parse_qs(parse_result.query)
        return dict_result['id'][0]

    def solveWbPath(self, url):
        self.originalUrl=url

        if self.wbpath == False:
            parse_result = urlparse(url)
            if parse_result.netloc=="web.archive.org":
                parts = parse_result.path.split('/')
                wbpath = "/"+parts[1]+"/"+parts[2]+"/"
                if wbpath[-1]=="_":
                    # this is a image or iframe link!
                    self.wbpath=wbpath[:-3]
                else:
                    self.wbpath=wbpath
            else:
                raise Exception("Href has no Wayback prefix!?")
       
        url=parse_result.path.replace(self.wbpath,"")
        if len(parse_result.query)>1:
            url = url+"?"+parse_result.query

        self.url=url



    def getHrefLink(self,url):
        # required!
        self.solveWbPath(url)

        return self.url
    
    def getIframeLink(self,url):
        # iframelinks have Wayback path suffix 'im_'
        # obsolete, replaced by solveWbPath
        return url.replace(self.wbpath+"if_/","")

    def getImageLink(self,url):
        # imagelinks have Wayback path suffix 'im_'
        # obsolete, replaced by solveWbPath
        return url.replace(self.wbpath+"im_/","")


    def parseWayBackUrl(self,value):
        parse_result = urlparse(value)
        #dict_result = parse_qs(parse_result.query)
        try :
            return parse_result #dict_result['c'][0]
        except Exception as e:
            print(e)
            exit()
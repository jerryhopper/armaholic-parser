
# import required module
import os,sys,time
from waybackpy import WaybackMachineCDXServerAPI
from bs4 import BeautifulSoup
import requests

from lib import fn_layoutparser

# assign directory
directory = 'cache'

startTime = time.time() 

fix=0 
# iterate over files in
# that directory
teller = 0
error = 0
idList=[]
for filename in os.listdir(directory):
    cachefile = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(cachefile):
        idList.append(int(cachefile.split(".")[0].split("_")[1])) 

print("Number of files: "+str(len(idList)))
idList.sort()

#print(idList)
#exit()


#print ('Number of arguments:'+ str(len(sys.argv))+' arguments.')
#print ('Argument List:'+ str(sys.argv))

try:
    startfromArmaholicId = int(sys.argv[1])
except Exception as e:
    startfromArmaholicId = 0
    pass
#print (sys.argv)
#exit()
unknownlist = []
errorLayouts = []
sectionlist = []
itemlist=[]
itemteller = 0
newsteller = 0
for armaholicId in idList:
    cachefile = "cache/page_"+str(armaholicId)+".html"
    #print("Cachefile: "+cachefile)
    #for filename in os.listdir(directory):
    #cachefile = os.path.join(directory, filename)

    # Skip function
    if armaholicId>startfromArmaholicId:


        # checking if it is a file
        if os.path.isfile(cachefile):
            #print(" ")
            teller +=1     
            
            try:
                f = open(cachefile,"r",encoding='utf-8')
                string = f.read()
                f.close()  
                #print("Reading "+cachefile)

                soup = BeautifulSoup(string, "html.parser")

                pagelayout = fn_layoutparser.parser(soup)
                
                pagelayout.foundLayout
                pagelayout.armaholicSection
                #pagelayout.armaholicId

                if pagelayout.page_title_element == None:
                    exit("Exit on id: "+ str(armaholicId) +" Layout:"+ str(pagelayout.foundLayout))
                #else:
                #    print(pagelayout.armaholicSection)
                #33000
                print("id: {id:5d}, l: {l:2d} s: {s:35} - {t}".format(id = armaholicId,l=pagelayout.foundLayout, s = pagelayout.armaholicSection, t=pagelayout.page_head_title))
                #detectedpage = fn_pagedetector.detector(string)
                
                #if detectedpage.page_is_valid == False:
                #    if detectedpage.page_template=="removed":
                #        os.remove(cachefile)
                #    #else:
                #    #    print(detectedpage.soup)
                #    #    print("AholicId: "+str(armaholicId))
                #    #    print(detectedpage)
                #    #exit("____") 
                
                #print(detectedpage.soup)
                #print("AholicId: "+str(armaholicId))
                #print(detectedpage)
                #exit("...")    
            except UnicodeDecodeError as e:
                print("UNICODE_ERROR "+armaholicId) 
                with open(cachefile+".error","wb") as fw:
                    fw.write(b"404")
                os.remove(cachefile)
                #exit()

            #
            
            part = pagelayout.armaholicSection[:4]
            if part=="arma":
                #print("PROCESS THE ITEM PAGE")
                itemteller +=1  
                if pagelayout.armaholicSection not in sectionlist:
                    sectionlist.append(pagelayout.armaholicSection)
                itemlist.append(str(armaholicId)+","+str(pagelayout.foundLayout)+","+pagelayout.armaholicSection  )
            elif part=="ofp_":
                #print("PROCESS THE ITEM PAGE")
                itemteller +=1  
                if pagelayout.armaholicSection not in sectionlist:
                    sectionlist.append(pagelayout.armaholicSection)
                itemlist.append(str(armaholicId)+","+str(pagelayout.foundLayout)+","+pagelayout.armaholicSection  )
            #    # 
            #    # do some parsing.
            #    #
            #    fn_pageparser.parser(detectedpage.soup)
            
            
            elif part =="news":
                #print("PROCESS NEWSPAGE")
                newsteller +=1
                if pagelayout.armaholicSection not in sectionlist:
                    sectionlist.append(pagelayout.armaholicSection)
            
            #    os.rename( cachefile, "newscache/page_"+str(armaholicId)+".html")  
            #    #"cache/page_"+str(armaholicId)+".html"
            #else:
            #    os.rename( cachefile, "unknowncache/page_"+str(armaholicId)+".html")  
            #f = open(cachefile,"r")
            #string = f.read()
            #f.close() 
            #print("'"+pagelayout.armaholicSection+"'")
            elif pagelayout.armaholicSection == "UNKNOWN":
                error +=1
                if pagelayout.foundLayout not in errorLayouts:
                    errorLayouts.append(pagelayout.foundLayout)

                if armaholicId not in unknownlist:
                    unknownlist.append(armaholicId)    
                


            
            #time.sleep(.1)

endTime = time.time()


print("total pages in cache :"+str(teller))
print("errorneous pages.... :"+str(error))
print("file items: "+str(itemteller))
print("news items: "+str(newsteller))
print("Parsing time: "+str(endTime - startTime)+" seconds.")

try:
    os.unlink("sectionlist.txt")
except:
    pass

f = open("sectionlist.txt", "w")
sectionlist.sort()
for dasection in sectionlist:
    #print(dasection)
    f.write(str(dasection)+"\n")
f.close()
print("SECTIONS: written to sectionlist.txt")


try:
    os.unlink("itemlist.txt")
except:
    pass

f = open("itemlist.txt", "w")
for daitem in itemlist:
    #print(dasection)
    f.write(str(daitem)+"\n")
f.close()
print("ITEMS: written to itemlist.txt")


try:
    os.unlink("unknownlist.txt")
except:
    pass
f = open("unknownlist.txt", "w")
for unknitem in unknownlist:
    #print(dasection)
    f.write(str(unknitem)+"\n")
f.close()
print("UNKNOWNS: written to unknownlist.txt")


#unknownlist

#print(itemlist)


#print("Layout with unknowns: ")
#print(errorLayouts)





exit()


def geturl():
    response = requests.get(self.URL)
    if response.status == 200:
        return response

def waybackUrls(url):
    user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    cdx = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=2010, end_timestamp=2021)
    #for item in cdx.snapshots():
    #    print(item.archive_url)
    return cdx.snapshots()
    


def waybackUrl(url,good=0,bad=0):
    user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    try:
        cdx_api = WaybackMachineCDXServerAPI(url, user_agent)
        
        newest = cdx_api.newest()
        #oldest = cdx_api.oldest()
        #print(oldest)
        #print(oldest.archive_url)
        #print(newest.archive_url)
        return newest.archive_url
    except Exception as e:
        print("404 "+url+" good: "+str(good)+" bad: "+str(bad)+" - "+ str(e)[0:70])
        #print( e )
        return False
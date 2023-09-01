import os, sys,time
from bs4 import BeautifulSoup
from lib import fn_layoutparser
from lib import fn_dataextractor

if not os.path.exists("itemlist.txt"):
    print("itemlist.txt not found.")
    print("consider running analyzeCache.py first!")

try:
    startfromArmaholicId = int(sys.argv[1])
except Exception as e:
    startfromArmaholicId = 0
    pass

import csv
rows = []
sections = {}
templates = {}
uniquelayouts = []

workerlist = {}

with open("itemlist.txt", 'r') as file:
    csvreader = csv.reader(file)
    #header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        row[0] #id
        row[1] #template
        row[2] #section
        if row[1] not in workerlist:
            workerlist[row[1]]=[]
            workerlist[row[1]].append(row[0])
        else:
            workerlist[row[1]].append(row[0])    

        if row[1] not in uniquelayouts:
            uniquelayouts.append(row[1])
        if row[2] in sections:
            if not row[1] in sections[row[2]]:
                sections[row[2]].append(row[1])
        else:
            sections[row[2]]=[]
            sections[row[2]].append(row[1])

        #break


## print sections and the layoutnumbers used.
#for item in sections:
#    print(item + " using layoutnumbers:" +str( sections[item] ))


print("\nUnique layouts used for ofp/arma files:")
print(uniquelayouts)

print("")
for layout in workerlist:
    print("Layout "+layout+" has "+str(len(workerlist[layout]))+" pages.")       

    i=0
    while i<len(workerlist[layout]):
        # the id.
        armaholicId=int(workerlist[layout][i])
        # the cachefile.
        cachefile = "cache/page_"+str(armaholicId)+".html"
        # 
        # armaholicId
        if armaholicId >= startfromArmaholicId: 
            if os.path.isfile(cachefile):
                    
                    # loading the html 
                    try:
                        f = open(cachefile,"r",encoding='utf-8')
                        string = f.read()
                        f.close()  
                        
                        # initializin BS
                        soup = BeautifulSoup(string, "html.parser")


                        pagelayout = fn_layoutparser.parser(soup)
                        print("l: "+str(pagelayout.foundLayout)+" aId: "+ str(pagelayout.armaholicId) +" "+pagelayout.armaholicSection)
                        

                        extractor = fn_dataextractor.extractor(pagelayout) 

                        #print(pagelayout.armaholicId)
                        #print(pagelayout.foundLayout)
                        #print(pagelayout.page_head_title)
                        #print(pagelayout.armaholicSection)
                        try:
                            extractor.extract()
                        except Exception as e:
                            print(e)
                        
                        #exit("-=Fin=-")



                    except UnicodeDecodeError as e:
                        print("UNICODE_ERROR "+armaholicId) 
                        #with open(cachefile+".error","wb") as fw:
                        #    fw.write(b"404")
                        #os.remove(cachefile)
                        exit()
            
        
        
        i +=1
        
#print(workerlist)


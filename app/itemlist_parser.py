import os, sys,time



if not os.path.exists("itemlist.txt"):
    print("itemlist.txt not found.")
    print("consider running analyzeCache.py first!")


import csv
rows = []
sections = {}
templates = {}
uniquelayouts = []

with open("itemlist.txt", 'r') as file:
    csvreader = csv.reader(file)
    #header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        row[0] #id
        row[1] #template
        row[2] #section
        if row[1] not in uniquelayouts:
            uniquelayouts.append(row[1])
        if row[2] in sections:
            if not row[1] in sections[row[2]]:
                sections[row[2]].append(row[1])
        else:
            sections[row[2]]=[]
            sections[row[2]].append(row[1])

        #break
#print(sections)
for item in sections:
    print(item + " using layoutnumbers:" +str( sections[item] ))

print("\nUnique layouts used for ofp/arma files:")
print(uniquelayouts)



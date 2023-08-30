import os, sys,time



if not os.path.exists("sectionlist.txt"):
    print("sectionlist.txt not found.")
    print("consider running analyzeCache.py first!")

f = open("sectionlist.txt", "r")
tlist = []
for x in f:
  tlist.append(x.strip())

tlist.sort()

for y in tlist:
   print(y)
import os, sys,time



if not os.path.exists("itemlist.txt"):
    print("itemlist.txt not found.")
    print("consider running analyzeCache.py first!")

f = open("itemlist.txt", "r")
tlist = []
for x in f:
  tlist.append(x.strip())

tlist.sort()

for y in tlist:
   print(y)
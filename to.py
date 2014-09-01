#!/bin/python 

fp = open("trackers.txt")

trackers = []

for l in fp.readlines() :
  l = l[:-1]
  if l == "" : continue
  if l not in trackers : trackers.append(l)
  
fp.close()

fp = open("trackers.txt", "w")
for l in trackers :
  fp.write(l+"\n\n")
fp.close()

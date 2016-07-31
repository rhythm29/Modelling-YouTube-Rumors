#!/usr/bin/env python
import sys
#with open("hi") as f:
#        content = f.readlines()
stri=""
for i in sys.stdin:
    i = i.strip().strip(" ");
    if(i.startswith('Video: ')):
#      print i  
      print stri.strip().strip(" ")
#      print "------------------------------------------------------------"
      stri = i
    else:
     stri = stri +" "+i.strip()


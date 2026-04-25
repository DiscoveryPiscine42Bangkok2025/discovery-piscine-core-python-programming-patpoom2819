#!/usr/bin/env python3

import sys
 
if len(sys.argv)>1:
    print("none")
    sys.exit()

i = 0
while i<11 :
    line = "Table de " + str(i) + ":"
    j=0
    while j<11:
        line += " "+str(j*i)
        j+=1

    print(line)
    i +=1
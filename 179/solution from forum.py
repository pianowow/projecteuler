#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     28/08/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from time import clock
clock()
max = 10**7;

acount=0;
div_count=[1]*max;
for n in range(2,max):
    for m in range(n,max,n): div_count[m]+=1;
    if(div_count[n]==div_count[n-1]): acount+=1;
print(clock())
print ("Acount = %d"%acount)
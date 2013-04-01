#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     27/11/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from itertools import permutations, count
from functools import reduce
from time import clock
from math import factorial
cnt = 0
max = 16
clock()

#three digits:
#A10, A01, 10A, 1A0
cnt += 4

#more digits:
for digits in range(4,max+1):
    print(digits,'digits')
    xcnt = digits - 3
    for x in permutations(range(digits),3): #position of 0,1, and A in that order
        print(x)
        if x[0] != 0: #zero is not in the first position
            if 0 not in x: #X is in the first position
                cnt += 15*16**(xcnt-1)
            else:
                cnt += 16**xcnt


lst = []
modcnt = cnt

while modcnt > 16:
    lst.append(modcnt % 16)
    modcnt -= modcnt % 16
    modcnt //= 16
print(lst)
lst.reverse()

dec = [10, 11, 12, 13, 14, 15]
hex = ['A','B','C','D','E','F']

for i,d in enumerate(dec):
    while d in lst:
        lst[lst.index(d)] = hex[i]


print(clock(), 'seconds')
print(cnt)

str = reduce(lambda x,y: str(x)+str(y),lst)

print(lst)
print(str)

#  853D5E


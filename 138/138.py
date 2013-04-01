#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     28/11/2012

from math import sqrt
from time import clock
clock()
BHLs = []
halfb = 1.5
max = 2000000000
squares = set()
##for x in range(max):
##    squares.add(x*x)
print('max:',max)
##while halfb < max:
##    b = 2*halfb
##    h1 = b-1
##    h2 = b+1
##    l1 = halfb*halfb + h1*h1
##    l2 = halfb*halfb + h2*h2
##    if l1 in squares:
##        BHLs.append((b,h1,l1))
##        print('base',b,'height',h1,'length',l1)
##    if l2 in squares:
##        BHLs.append((b,h2,l2))
##        print('base',b,'height',h2,'length',l2)
##    halfb += .5
##print(clock(), 'seconds')

#terms for b printed above follow the pattern of every third term of A121646 from oeis, negated
#so I decided to generate this sequence and check each one

t0 = 1
t1 = 1
t2 = 2
b = t2*t2-t1*t1
sumofLs = 0
while len(BHLs) < 12:
    halfb = b/2
    h1 = b-1
    h2 = b+1
    l1 = sqrt(halfb*halfb + h1*h1)
    #l2 = sqrt(halfb*halfb+h2*h2)
    l2 = sqrt(halfb*halfb + h2*h2)
    if l1 % 1 == 0:
        BHLs.append((b,h1,l1))
        print('base',b,'height',h1,'length',l1)
        sumofLs += int(l1)
        print('sum of Ls so far:',sumofLs)
    if l2 % 1 == 0:
        BHLs.append((b,h2,l2))
        print('base',b,'height',h2,'length',l2)
        sumofLs += int(l2)
        print('sum of Ls so far:',sumofLs)
    t0,t1 = t1, t2
    t2 = t0+t1
    b = t2*t2-t1*t1
print(len(BHLs),'found')
print(sumofLs)
print(clock(), 'seconds')
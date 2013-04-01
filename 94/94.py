#-------------------------------------------------------------------------------
# Name:        94
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     29/08/2012

##It is easily proved that no equilateral triangle exists with integral length
##sides and integral area. However, the almost equilateral triangle 5-5-6 has
##an area of 12 square units.
##
##We shall define an almost equilateral triangle to be a triangle for which two
##sides are equal and the third differs by no more than one unit.
##
##Find the sum of the perimeters of all almost equilateral triangles with
##integral side lengths and area and whose perimeters do not exceed one
##billion (1,000,000,000).

#attempt 1
##from math import sqrt
##from time import clock
###max = 333333333
##max = 100
##
##perimetertotal = 0
##
##clock()
##for samesides in range(3,max+1):
##    otherside = samesides - 1
##    height = sqrt(samesides**2-(otherside/2)**2)
##    twicearea = height*otherside
##
##    if twicearea%2 == 0:
##        print (samesides, samesides, otherside, height, twicearea/2)
##        perimetertotal += (samesides*2+otherside)
##    otherside = samesides + 1
##    height = sqrt(samesides**2-(otherside/2)**2)
##    twicearea = height*otherside
##
##    if twicearea%2 == 0:
##        print (samesides, samesides, otherside, height, twicearea/2)
##        perimetertotal += (samesides*2+otherside)
##
##print('went to',max,'in',clock(),'seconds')
##print('sum of perimeters:',perimetertotal)

from math import sqrt
from time import clock
max = 333333333
#max = 100

perimetertotal = 0

clock()

x = 2
y = 1

samesides = (2*x-1)/3
area = y*(x-2)/3
otherside = samesides + 1

if samesides%1==0 and area%1==0 and area>0 and samesides>0 and otherside> 0:
    perimetertotal+=(samesides*2+otherside)


samesides = (2*x + 1)/3
area = y*(x-2)/3
otherside = samesides - 1

if samesides%1==0 and area%1==0 and area>0 and samesides>0 and otherside> 0:
    perimetertotal+=(samesides*2+otherside)

while ((samesides*2+otherside)<=max):

    samesides = (2*x-1)/3
    area = y*(x-2)/3
    otherside = samesides - 1

    if samesides%1==0 and area%1==0 and area>0 and samesides>0 and otherside> 0:
        perimetertotal+=(samesides*2+otherside)
        print(samesides,samesides,otherside,area)


    samesides = (2*x + 1)/3
    area = y*(x+2)/3
    otherside = samesides + 1

    if samesides%1==0 and area%1==0 and area>0 and samesides>0 and otherside> 0:
        perimetertotal+=(samesides*2+otherside)
        print(samesides,samesides,otherside,area)

    x,y = 2*x+3*y,2*y+x

print('went to',max,'in',clock(),'seconds')
print('sum of perimeters:',perimetertotal)
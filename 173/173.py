#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     05/09/2012

##We shall define a square lamina to be a square outline with a square "hole" so
##that the shape possesses vertical and horizontal symmetry. For example, using
##exactly thirty-two square tiles we can form two different square laminae.
##
##With one-hundred tiles, and not necessarily using all of the tiles at one time,
##it is possible to form forty-one different square laminae.
##
##Using up to one million tiles how many different square laminae can be formed?
from time import clock
max = 1000000
count = 0
clock()
for holeSide in range(1,int(max/4)):
    #1block all the way around
    t = 1
    numBlocks = (holeSide+t)*4
    while numBlocks <= max:
        count += 1
        t+=2
        numBlocks += (holeSide+t)*4
print (count, clock(), 'seconds')
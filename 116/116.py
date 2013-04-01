#-------------------------------------------------------------------------------
# Name:        116
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     28/08/2012

##A row of five black square tiles is to have a number of its tiles replaced
##with coloured oblong tiles chosen from red (length two), green (length three),
## or blue (length four).
##
##If red tiles are chosen there are exactly seven ways this can be done.
##
##If green tiles are chosen there are three ways.
##
##And if blue tiles are chosen there are two ways.
##
##Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
##replacing the black tiles in a row measuring five units in length.
##
##How many different ways can the black tiles in a row measuring fifty units in
##length be replaced if colours cannot be mixed and at least one coloured tile
##must be used?
##
##NOTE: This is related to problem 117.
from copy import copy
from time import clock

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

max = 50
uniquelists = []
#generate the unique lists of tiles to use
def listtiles(blockSize, size):
    maxBlocks = size // blockSize
    for blockCount in range(1, maxBlocks+1):
        lst = [blockSize]*blockCount
        while sum(lst) < size:
            lst.append(1)
        yield lst

#order the unique lists
def listorders(start, rest):
    global nonuniquelists
    #print('arrived with start',start,'rest',rest)
    if rest == []:
        if start not in uniquelists:
            uniquelists.append(start)
            print(start)
    for item in rest:
        newrest = copy(rest)
        newrest.remove(item)
        newstart = copy(start)
        newstart.append(item)
        #print('calling listorders with arguments start', newstart, 'rest', newrest)
        if len(newrest)*newrest[0] == sum(newrest): #if all the rest are the same element, no need to continue
            if newstart+newrest not in uniquelists:
                uniquelists.append(newstart+newrest)
                print(newstart+newrest)
        else:
            listorders(newstart, newrest)

clock()
count = 0
prevcount = 0
for blocksize in range(2,5):
    for tilelist in listtiles(blocksize,max):
        #listorders([], tilelist)   #speed of this increases WAY too fast
        #count += len(uniquelists)
        tilecount = len(tilelist)
        blocktiles = tilelist.count(blocksize)
        count += choose(tilecount,blocktiles)
        uniquelists = []
    print('seconds elapsed:',clock())
    print(blocksize, count-prevcount)
    prevcount = count


print('total',count)
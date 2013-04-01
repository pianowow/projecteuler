#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     29/11/2012

#some  change here

#2**N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.
#For N=3, two such circular arrangements are possible, ignoring rotations.

#For the first arrangement, the 3-digit subsequences, in clockwise order, are:
#000, 001, 010, 101, 011, 111, 110 and 100.
#second is:
#000, 001, 011, 111, 110, 101, 010 and 100

#Each circular arrangement can be encoded as a number by concatenating the binary digits starting
#with the subsequence of all zeros as the most significant bits and proceeding clockwise.
#The two arrangements for N=3 are thus represented as 23 and 29:

#   00010111 = 23
#   00011101 = 29

#Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.

#Find S(5).

#----------------

#analysis
#2**5 is 32 digits
#2**32 is a huge search space (4,294,967,296)
#but, given that the first 5 digits are 0 and the 6th digit is nonzero, we are left with only 26 binary digits
#2**26 is only (67,108,864)
#so that is in the realm of brute force
#we also know the last digit is 1... so that reduces the search space to
#2**25 = 33,554,432

from itertools import product
from functools import reduce
from time import clock

N = 5 #N

def circleisgood(circle):
    subsequences = set()
    #add first 2**N - 1 digits to the end
    newcircle = circle + circle[0:N-1]
    #check every N digits for uniqueness starting from 0 to 2**N
    for x in range(2**N):
        subseq = newcircle[x:x+N]
        #print (subseq)
        if subseq in subsequences:
            return False
        else:
            subsequences.add(subseq)
    return True

#circles are of the form 0001___1  (if N = 3 for example)
#so you have 2**N - N - 2 digits to actually discover
variablelen = 2**N - N - 2
beginning = '0'*N + '1'
ending = '1'

def bintodec(binstr):
    length = len(binstr)
    power = 2**(length-1)
    val = 0
    for i in range(length):
        digit = binstr[i]
        power = length-1-i
        if digit == '1':
            val += 2**power
    return val

ttl = 0
clock()
for variable in product('10', repeat=variablelen):
    variablestr = reduce(lambda x,y:str(x)+str(y), variable)
    circle = beginning + variablestr + ending
    if circleisgood(circle):
        print (circle)
        ttl += bintodec(circle)
print (ttl)
print(clock(), 'seconds')
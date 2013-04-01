#-------------------------------------------------------------------------------
# Name:        179
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     27/08/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#  Find the number of integers 1  n  107, for which n and n + 1 have the same
#  number of positive divisors. For example, 14 has the positive divisors 1,
#  2, 7, 14 while 15 has 1, 3, 5, 15.

from time import clock
from math import sqrt

limit = 10000000

Divisors = 0
prevDivisors = 2 #2 has 2 divisors
cnt = 0

clock()

for N in range(3, limit):
    Divisors = 2 #(1,N)
    sqr = int(sqrt(N))
    if pow(sqr,2) == N:
        Divisors = -1  #square numbers are the only numbers with odd divisor count
##        Divisors += 1
##        for x in range(2, sqr):
##            if N%x == 0:
##                Divisors += 2
        #print('looking at '+str(N)+', found '+str(Divisors)+' divisors, '+'searched through '+str(sqrt-1))
    else:
        for x in range(2, sqr+1):
            if N%x == 0:
                Divisors += 2
        #print('looking at '+str(N)+', found '+str(Divisors)+' divisors, '+'searched through '+str(sqrt))
    if Divisors == prevDivisors:
        cnt+=1
        #print ('Found: ' + str(N-1) + ', ' + str(N) +'.',cnt,'so far')
    prevDivisors = Divisors

print( clock())
print(cnt,'pairs found under', limit)
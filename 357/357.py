#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     29/11/2012

from math import sqrt
from time import clock

prime = {2,3,5,7}

def sieve(maximum):
    #1 means prime
    #0 means composite
    lst = [1]*maximum
    lst[0] = 0
    lst[1] = 0
    siever = lst.index(1)
    while siever*siever < maximum:
        composite = siever*siever
        while composite < maximum:
            lst[composite] = 0
            composite += siever
        siever = lst.index(1,siever+1)
    return lst

##def is_prime(n):
##    if n in prime:
##        return True
##    elif n % 2 == 0 or n % 3 == 0:
##        return False
##    r = int(sqrt(n))
##    f = 5
##    while f <= r:
##        if n % f == 0 or n % (f + 2) == 0:
##            return False
##        else:
##            f += 6
##    prime.add(n)
##    return True
##
##def test_factors(n):
##    sq = int(sqrt(n))
##    if sq ** 2 == n:
##        return False
##    for x in range(1, sq + 1):
##        if n % x == 0:
##            if not is_prime(x + n/x):
##                return False
##    return True

##clock()
##max = 100000000
##ttl = 1  #1 satisfies this test, but it's the only odd number that does
##test = 1000000
##for x in range(2,max+1,2):
##    if test_factors(x):
##        ttl += x
##        if x > test:
##            print(x, ttl, clock(),'seconds')
##            test += 1000000
##print(ttl, clock(),'seconds')



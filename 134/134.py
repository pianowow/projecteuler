#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     18/09/2012
from time import clock
def find_primes_less_than(n):
    not_p = set()
    primes = []
    for i in range(2, n):
        if i not in not_p:
            primes.append(i)
            for j in range(i * 2, n, i):
                not_p.add(j)
    return primes

primes = find_primes_less_than(1000004)

##for i in range(2,primecount-1):
##    p1 = primes[i]
##    p2 = primes[i+1]
##
##    digits = len(str(p1))
##    add = 10**digits
##    num = p1+add
##    while num%p2 != 0:
##        num += add
##    if i%percent == 0:
##        print(p1,p2,num)
##    ttl += num
##
##print(ttl)



#euler 134

# generate prime list
##import time
##t0 = time.time()
##import math

##def sieve(n):
##    initSieve = []
##    maxNum = int(math.sqrt(n))+1
##    for i in range(2,n):
##        initSieve.append(True)
##    j = 2
##    while j <= maxNum:
##        if initSieve[j-2]:
##            for k in range(j*j, n, j):
##                initSieve[k-2] = False
##        j += 1
##    outputList = [x+2 for x in range(len(initSieve)) if initSieve[x]]
##    return outputList

##factors = sieve(1000000)

##def isprime(n):
##    n*=1.0
##    if n%2==0 and n!=2 or n%3==0 and n!=3:
##        return False
##    for b in range(1,int((n**0.5+1)/6.0+1)):
##        if n%(6*b-1)==0:
##            return False
##        if n %(6*b+1)==0:
##           return False
##    return True
##
##extraP = 1000000
##while not isprime(extraP):
##    extraP += 1
##factors.append(extraP)



# use extended euclidean algorithm (from Wikipedia)

def exgcd(a,b):
    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while b != 0:
        quotient = a//b
        a, b = b, a%b
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient *y, y
    return lastx, lasty, a

# pr function will return two number p1, p2 based on index of prime sieve
# i.e. pr(7) returns 19, 23
# we want the second number, p2, to be the base for our modulus (i.e mod 23)
# we want to solve equation of the form
# 100 * x + 19 is congruent to 0 mod 23
# which is 100 * x is congruent to 4 mod 23
# the 100 is based on the length of p1, i.e. if p1 is 2 digits, then take 10^2
# The solution of the linear congruence: ax is congruent to b mod n
# is x = rb/d where
# r is returned by our extended euclidean algorithm
# ra + sn =d (our function exgcd of a, b returns lastx, lasty, a and
# in this case r is last x
# d is the gcd, and since we are always looking at 2 primes, this is always 1

def solvelc(p1, p2):
    a = 10**len(str(p1))
    b = p2-p1
    n = p2
    r, s, d = exgcd(a,n)
    x = r*b
    x = x % n  # take modulus to find lowest x in congruent set
    return x*a + p1

def pr(index):  # takes index
    p1 = primes[index]
    p2 = primes[index+1]
    return p1, p2

clock()
answer = 0
for i in range(2, len(primes)-1):
    p1, p2 = pr(i)
    temp = solvelc(p1,p2)
    answer += temp
##    print p1, p2, temp, answer

print(clock(),'seconds')
print (answer)
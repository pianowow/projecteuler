#-------------------------------------------------------------------------------
# Name:        214
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     29/10/2012

#totient chains

from time import clock
from itertools import combinations

def find_primes_less_than(n):
    not_p = set()
    primes = []
    for i in range(2, n):
        if i not in not_p:
            primes.append(i)
            for j in range(i * 2, n, i):
                not_p.add(j)
    return primes

savedphi = {1:1, 2:1}
savedphichainlength = {1:1, 2:2}

def phi(n):
    result = n
    i = 2
    if n in savedphi:
        return savedphi[n]
    while i ** 2 <= n:
        if n % i == 0:
            result -= result // i
        while n % i == 0:
            n //= i
        i += 1
    if n > 1:
        result -= result // n
    savedphi[n] = result
    return result

def phichainlength(n):
    if n in savedphichainlength:
        return savedphichainlength[n]
    x=n
    increments = 1
    while x != 1:
        x = phi(x)
        increments += 1
    savedphichainlength[n] = increments
    return increments

clock()
maximum = 100000
searchlen = 10
print('finding primes less than',maximum)
primes = set(find_primes_less_than(maximum))

print('sieving totient numbers')
for prime in primes:
    i = 1
    prevpower = 1
    power = prime
    while power < maximum:
        savedphi[power] = power - prevpower
        i+=1
        prevpower = power
        power = prime**i

foundprimes = set()
print('searching for primes with totient chain length',searchlen)
for prime in primes:
    if phichainlength(prime-1) +1 == searchlen:
        foundprimes.add(prime)

print(clock(),'seconds')
print(sum(foundprimes))


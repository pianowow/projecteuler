#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Francky
#
# Created:     30/11/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from time import clock
print(clock(),'sieving primes')
limit=10**8
#limit=100
lim=limit+2
prime = bytearray([True])*(lim+1)
prime[:2] = bytearray(2)
prime[4::2] = bytearray(limit>>1)
for i in range(3, int(lim**0.5)+1, 2):
    if prime[i]:
        prime[i*i::i]=bytearray(lim//i-i+1)

res = 1
print(clock(),'checking numbers')
for n in range(2, limit+1, 4): # killer : step by 4
  if prime[n+1] and prime[n//2+2] and \
  all(prime[d+n//d] for d in range(3, int(n**0.5)+1) if not n%d):
    res+=n
print(clock(),res)
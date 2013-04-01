#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      andrewstewart25
#

from time import clock

maximum = 40000000
searchlen = 25

def find_primes_less_than(n):
    not_p = set()
    primes = []
    for i in range(2, n):
        if i not in not_p:
            primes.append(i)
            for j in range(i * 2, n, i):
                not_p.add(j)
    return primes

clock()
print('finding primes less than',maximum)
primes=find_primes_less_than(maximum+1)

def phitable(n):
  phis2=list(range(n+1))
  for p in primes:
    for multp in range(p,n+1,p):
      phis2[multp]=(phis2[multp]//p)*(p-1)
  return phis2

def blah(n,length):
  print('sieving totient numbers')
  phi=phitable(n)
  backprimes=primes[::-1]
  x=0
  print('searching for primes with totient chain length',searchlen)
  for p in backprimes:
    a=p
    b=1
    while a>1:
      a=phi[a]
      b+=1
    if b==length:x+=p
  return x


print(blah(maximum, searchlen))
print(clock(),'seconds')
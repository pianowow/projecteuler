#-------------------------------------------------------------------------------
# Name:        129
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN


#the difference between n and k has been quite small even as n increases.  I modified A to start searching around n because of this.

#pretty sure that
#R(k) mod n = (((10**(k)) mod n) - 1)/(9 mod n)  (or something like this)
#that enables us to use the super fast pow function to calculate pow(10,k+1,n) very fast

#99,911 seems to be a very tricky number to get A(n) for.
#giving the loop a maximum of 100,000 got to 99,911 and stopped



from fractions import gcd
from itertools import count
from time import clock


def RKmodN(k,n):
    x = (pow(10,k,n)-1)%n  #99999... %n  #becomes a problem when n divides 9999... but not 1111...
    print('x =',x)
##    if x==y==0: return 0
##    if n%9 != 0:
    if n!=9:
        for i in range(1,n+1):
            if (i*9)%n == x:  #if n==9 this expression is always true
                print('i = ',i,'i*9%n = ', x)
                return i




def A(n):
    '''given n with gcd(n,10)= 1,
    computes k such that a repunit of length k
    is the smallest repunit that is evenly divided by n'''
    if gcd(n,10) == 1:
##        for lengthdiff in count(1):
##            length = n-lengthdiff
##            if length > 0:
##                print('trying length',length)
##                if RKmodN(length,n) == 0:
##                    return length
##            length = n+lengthdiff
##            print('trying length',length)
##            if RKmodN(length,n) == 0:
##                    return length
        x = 1
        k = 1
        while x > 0:
            x = (10*x+1) % n
            k+=1
        return k
    else:
        return 0

limit = 1000001
n = limit
while A(n)<limit: n += 2
print(n)

##print('finding the smallest divisor of repunit of length k, such that k is greater than',maximum)
##
##clock()
##maxsofar = 0
##greatestdifference = 0
##n = 0
##k = 0
##for n1 in count(maximum//10-10):
##    for n0 in [1,3,7,9]: #numbers ending in 1,3,7,9 are the only ones that satisfy gcd(10,n) == 1
##        n = n1*10+n0
##        print('trying',n)
##        k = A(n)
##        if k > maxsofar:
##            print(n,k)
##            diff = abs(n-k)
##            if diff > greatestdifference:
##                greatestdifference = diff
##            maxsofar = k
##        if k > maximum:
##            break
##    if k > maximum:
##        break
##print(n,k)
##print('biggest difference:',greatestdifference)
##print(clock(),'seconds')


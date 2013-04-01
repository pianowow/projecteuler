#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     18/09/2012
#light
from math import sqrt
from copy import copy


def Atkins(limit):
    is_prime = dict()
    keys = list(range(5,limit+1))
    for i in keys:
        is_prime[i]= False

    sqrt_limit = sqrt(limit)
    xys = list(range(1,int(sqrt_limit)+1))
    for x in xys:
        for y in xys:
            n = 4*(x*x) + (y*y)
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*(x*x) + (y*y)
            if (n <= limit and (n % 12 == 7)):
                is_prime[n] = not is_prime[n]
            n = 3*(x*x) - (y*y)
            if ((x>y) and n <= limit and (n % 12 == 11)):
                is_prime[n] = not is_prime[n]

    for i in keys:
        if is_prime[i]:
            max = limit // (i*i)
            for k in range(1,max+1):
                is_prime[k*(i*i)] = False

    yield 2;
    yield 3;
    for i in keys:
        if is_prime[i]:
            yield i

primes = list(Atkins(100))


def SumOfFactors( n, p):
    nt = copy(n)
    sm = 0
    while (nt > 0):
            nt = nt // p
            sm += nt
    return sm

n = 10
k = 3
sum = 0
for i in primes:
    sum += (SumOfFactors(n, i) - SumOfFactors(k, i) - SumOfFactors(n-k, i))* i

print(sum)
##
##Console.WriteLine "Primes Finished"
##let sw = new Stopwatch()
##sw.Start()
##Console.WriteLine  (Problem231 20000000UL 15000000UL)
##sw.Stop()
##Console.WriteLine(sw.Elapsed)
##Console.ReadLine() |> ignore
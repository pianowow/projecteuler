#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     07/09/2012


##x,y,n are positive integers:

##1/x+1/y = 1/n

##It can be verified that when n = 1260 there are 113 distinct solutions and
##this is the least value of n for which the total number of distinct solutions
##exceeds one hundred.

##What is the least value of n for which the number of distinct solutions exceeds four million?


primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
limit = 8000000
total = 1
x = 0
while total < limit:
    total *= 3
    x += 1
print (primes[x-1])
print(total)
print(x)

##(rest done by hand)
##
##start with first 15:
##2,3,5,7,11,13,17,19,23,29,31,37,41,43,47
##leads to
##3**15 = 14348907 solutions
##replacing 47 with 2*3 (6)
##5*5*3**12 = 13286025 solutions
##replacing 43 with 2*3 (6)
##7*7*3**11 = 8680203 solutions
##replacing 41 with 5*7 (35)
##7*7*5*5*3**8 = 8037225 solutions
##replacing 37 (can not do it!)
##
##so 2**3*3**3*5**2*7**2*11*13*17*19*23*29*31*37 = 9350130049860600 is the answer
##
##
##36 2**2*3**2
##35 5*7
##34 2*17
##33 3*11
##32 2**5
##30 2*3*5
##28 2**2*7
##27 3**3
##26 2*13
##25 5**2
##24 2**3 * 3
##22 2*11
##21 3*7
##20 2**2*5
##18 2*3**2
##16 2**4
##15 3*5
##14 2*7
##12 2**2*3
##10 2*5
##9 3**2
##8 2**3
##6 2*3
##4 2**2
##
##
##
##

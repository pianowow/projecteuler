#-------------------------------------------------------------------------------
# Name:        323
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     30/11/2012
from itertools import count
##from random import randrange
##from time import clock
###testing binary representation
##goal = int('1'*32,2)
##print('goal:',goal)
##
###bitwise or is |
##
##
###randrange(0,goal+1,1) gets us a random element evenly distributed in the range defined
##histogram = [0]*60
##tries = 0
##prevaverage = [0]*6
##average = 0
##precision = 2
##while True:
##    intermediate = randrange(0,goal+1,1)
##    steps = 0
##    while intermediate != goal:
##        nxt = randrange(0,goal+1,1)
##        intermediate |= nxt
##        steps += 1
##    histogram[steps] += 1
##    prevaverage[0],prevaverage[1],prevaverage[2],prevaverage[3],prevaverage[4],prevaverage[5] = average, prevaverage[0], prevaverage[1],prevaverage[2],prevaverage[3],prevaverage[4]
##    #average = round((steps+average*tries)/(tries+1),10)
##    tries += 1
##    ttl = 0
##    weight = 0
##    for step,freq in enumerate(histogram):
##        weight += step*freq
##    average = weight/tries
##    roundedaverage = round(average,precision)
##    roundedprevaverage = round(prevaverage[5],precision)
##    #print(prevaverage,average,tries)
##    if roundedaverage == roundedprevaverage and tries > 10:
##        print(roundedaverage,precision, tries)
##        print(histogram)
##        if precision == 10:
##            break
##        precision += 1
##
##print (average)




##/*
## * Suppose that n 32-bit integers have been OR'd together.
## * For any arbitrary digit:
## *   The probability that it is 0 is 1/2^n.
## *   The probability that it is 1 is 1 - 1/2^n.
## * Thus for the entire number:
## *   The probability that all digits are 1 is (1 - 1/2^n)^32.
## *     This is the cumulative distribution function that we want.
## *   The probability that some digit is 0 is 1 - (1 - 1/2^n)^32.
## *
## * The probability distribution function is simply pdf(n) = cdf(n) - cdf(n-1).
## * So the expected value of the index where the number becomes all 1's is
## * sum(n * pdf(n) for n = 0 to infinity).
## */

##	// Computes an approximate answer using floating-point; not guaranteed to be correct.
##	// However, the Mathematica version of the solution is exact.

def cdf(n):
    return (1 - 2**-n)**32

sum = 0.0
for n in count(1):
    p = cdf(n) - cdf(n - 1)
    if (p < 10**-20):  #// Truncate the series by ignoring insignificant contributions to the sum
        break
    sum += n * p
#return String.format("%.10f", sum);
print(round(sum,10))



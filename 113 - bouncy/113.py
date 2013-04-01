#-------------------------------------------------------------------------------
# Name:        113
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#


##Working from left-to-right if no digit is exceeded by the digit to its left
##it is called an increasing number; for example, 134468.
##
##Similarly if no digit is exceeded by the digit to its right it is called a
##decreasing number; for example, 66420.
##
##We shall call a positive integer that is neither increasing nor decreasing
##a "bouncy" number; for example, 155349.
##
##As n increases, the proportion of bouncy numbers below n increases such that
##there are only 12951 numbers below one-million that are not bouncy and only
##277032 non-bouncy numbers below 10**10.
##
##How many numbers below a googol (10**100) are not bouncy?


#represent an N digit number using N1s and X0s, where X is the number digits
#allowed
#example
#http://mathschallenge.net/full/never_decreasing_digits

from time import clock

length = 10000

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

#count increasing
#[length] 1s and 9s
clock()
increasing = choose(length+9, length) - 1
#print('increasing:', increasing)

#count decreasing
#all digits 9-0
decreasing = 0
new = 0
for x in range(1,length+1):
    new = choose(x+9, x) - 10 #0 and all same digit
    decreasing+=new
    #print('length:',x,'decreasing:', new)

#subtract duplicates (all the same digit)
#length-digit numbers of all the same number
total = increasing + decreasing

print(clock(),'seconds')
print('total under 10^'+str(length)+':',total)
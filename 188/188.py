#-------------------------------------------------------------------------------
# Name:        188
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/09/2012

def hyper_exp(a, b, m):
    temp = 1
    while b:
        temp = pow(a, temp, 10**m)
        b -= 1
    return temp

print(hyper_exp(1777, 1855, 8))
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     19/09/2012
from time import clock

MAX_SUM = 9
NUM_OF_DIGIT = 20
count = [[[0 for x in range(NUM_OF_DIGIT)] for x in range(10)] for x in range(10)]


def getCount(d1, d2, remainDigits):
    if (remainDigits == 0):
        return 1;
    else:
        if (count[d1][d2][remainDigits] == 0):
            ttl = 0
            for i in range(MAX_SUM-(d1+d2)+1):
                ttl += getCount(d2, i, remainDigits-1);
            count[d1][d2][remainDigits] = ttl
        return count[d1][d2][remainDigits];


clock()
result=0;

for i in range(1,10):
    result += getCount(0, i, NUM_OF_DIGIT-1);
print(clock(), 'seconds')
print(result)


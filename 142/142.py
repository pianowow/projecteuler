#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     28/11/2012

from itertools import permutations
from time import clock
#Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.

#method:
# 0. Cache perfect squares up to a maximum
# 1. Find squares who sum to another square. i.e., s1 + s2 = s3 so that... x - y = s1, y - z = s2, x - z = s3
# 2. Add n to s1, s2 to get n1 = n , n2 = n + s1, n3 = n + s1 + s2 (n1, n2, n3 will all have differences as perfect squares)
# 3. check n1+n2, n2+n3, and n1+n3 to see if they are all perfect squares

# ex: s1 9 s2 16 s3 25
#      n 1
#     n1 1 n2 10 n3 26
#     check 1+10, 10+26 and 1+26 to see if they are perfect squares

clock()
max = 1000
print('max:',max)
print('making list of squares')
maxsq = max*max
squares = set()
x = 1
while x < max:
    squares.add(x*x)
    x += 1

print('making list of sets of squares that satisfy s1+s2=s3')
diffsets = []
for s1,s2 in permutations(squares,2):
    s3 = s1+s2
    if s3 in squares:
        #print(s1,s2,s3)
        diffsets.append((s1,s2))

print('finding 3 perfect numbers')
perfectsets = []
for s1,s2 in diffsets:
    n = 0
    while (n+s1+s2)+(n+s1) < maxsq: #sum of the biggest two
        n1 = n
        n2 = n + s1
        n3 = n + s1 + s2
        #n1,n2,n3 all have differences of perfect squares
        #check if they add to perfect squares
        if n1+n2 in squares:
            if n1+n3 in squares:
                if n2+n3 in squares:
                    perfectsets.append((n1,n2,n3))
                    print(n1,n2,n3,'sum:',n1+n2+n3)
        n += 1

print(clock(),'seconds')
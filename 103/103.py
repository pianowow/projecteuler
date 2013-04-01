#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     18/09/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from itertools import *
from functools import reduce
from math import ceil

d = {}
def filt_func(c1, c2):
    if c1[0] > c2[0]:
        return False
    return not reduce(lambda x, y: x and (y[0] < y[1]), zip_longest(sorted(c1), sorted(c2)), True)


def generator(n, k):
    if (n, k) in d:
        return d[(n, k)]
    s1 = combinations(range(n), k // 2)
    comb_total = []
    for comb1 in s1:
        left_nums = set(range(n)) - set(comb1)
        s2 = (c for c in combinations(left_nums, k // 2) if filt_func(comb1, c))
        comb_total.extend(product([comb1], s2))
    d[(n, k)] = comb_total
    return comb_total

def check_cond1(s):
    for i in range(4, len(s) + 1, 2):
        for c1, c2 in generator(len(s), i):
            if sum(map(lambda x: s[x], c1)) == sum(map(lambda x: s[x], c2)):
                return False
    return True

def check_cond2(s):
    for i in range(2, ceil(len(s) / 2) + 1):
        if sum(s[:i]) <= sum(s[-(i - 1):]):
            return False
    return True

last = 0
for a in combinations(range(19, 48), 7):
	if check_cond1(a) == True and check_cond2(a) == True:
		print (a)
		break
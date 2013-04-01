#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     18/09/2012
from itertools import combinations, product, zip_longest
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


sets = []
for l in open('sets.txt'):
    s = sorted(map(int, l.strip().split(',')))
    sets.append(s)
result = sum(sum(s) for s in sets if check_cond2(s) and check_cond1(s))
print("The result is:", result)



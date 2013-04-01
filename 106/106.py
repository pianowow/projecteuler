#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
from itertools import zip_longest, combinations, product
from functools import reduce

def filt_func(c1, c2):
    if c1[0] > c2[0]:
        return False
    return not reduce(lambda x, y: x and (y[0] < y[1]), zip_longest(sorted(c1), sorted(c2)), True)

def generator(n, k):
    s1 = combinations(range(n), k // 2)
    comb_total = []
    for comb1 in s1:
        left_nums = set(range(n)) - set(comb1)
        s2 = (c for c in combinations(left_nums, k // 2) if filt_func(comb1, c))
        comb_total.extend(product([comb1], s2))
    return comb_total


result = sum(len(generator(12, i)) for i in range(4, 13, 2))
print("The result is:", result)
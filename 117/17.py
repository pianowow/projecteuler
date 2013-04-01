#-------------------------------------------------------------------------------
# Name:        117
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN

##Using a combination of black square tiles and oblong tiles chosen from: red tiles
##measuring two units, green tiles measuring three units, and blue tiles measuring
##four units, it is possible to tile a row measuring five units in length in
##exactly fifteen different ways.
##
##How many ways can a row measuring fifty units in length be tiled?
##
##NOTE: This is related to problem 116.

from time import clock

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

max = 5
uniquelists = []
#generate the unique (unordered) lists of tiles to use
def listtiles(size):
    max4 = size // 4
    for count4 in range(max4+1):
        list4 = [count4]
        max3 = (size - 4*count4) // 3
        for count3 in range(max3+1):
            list3 = list4 + [count3]
            max2 = (size - 4*count4 - 3*count3) // 2
            for count2 in range(max2+1):
                list2 = list3 + [count2]
                num1 = (size - 4*count4 - 3*count3 - 2* count2)
                lst = list2 + [num1]
                uniquelists.append(lst)
clock()
listtiles(max)
arrangementtotal = 0

for lst in uniquelists:
    total = lst[0]*4 + lst[1]*3 + lst[2]*2 + lst[3]
    if total != max:
        print('error:',lst, total)
    else:
        arrangement4 = choose(sum(lst),lst[0])
        arrangement3 = choose(sum(lst)-lst[0], lst[1])
        arrangement2 = choose(sum(lst)-sum(lst[0:2]),lst[2])
        print(lst)
        print('arrangement4',arrangement4)
        print('arrangement3',arrangement3)
        print('arrangement2',arrangement2)
        arrangements =arrangement4*arrangement3*arrangement2
        print('arrangements',arrangements)
        arrangementtotal += arrangements
#print(uniquelists)
print('arrangements:',arrangementtotal)

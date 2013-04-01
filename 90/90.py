#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     06/09/2012

from copy import copy

squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
#first digits: 0,1,2,3,4,4,8  (7)
#second digits: 1,4,5,6,9     (5)
digits = list(range(10))

def dice():
    for n1 in range(5):
        for n2 in range(n1+1,6):
            for n3 in range(n2+1,7):
                for n4 in range(n3+1,8):
                    for n5 in range(n4+1,9):
                        for n6 in range(n5+1,10):
                            yield set([n1,n2,n3,n4,n5,n6])


cnt = 0

for d1 in dice():
    md1 = copy(d1)
    if 6 in d1 or 9 in d1:
        md1.add(9)
        md1.add(6)
    for d2 in dice():
        md2 = copy(d2)
        if 6 in d2 or 9 in d2:
            md2.add(9)
            md2.add(6)
        allvals = set([str(n)+str(m) for n in md1 for m in md2]).union(set([str(m)+str(n) for n in md1 for m in md2]))
        #print(allvals)
        if len([x for x in squares if x not in allvals]) == 0:
            cnt += 1
            #print(d1,d2)

print(cnt/2)
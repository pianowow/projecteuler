#-------------------------------------------------------------------------------
# Name:        93
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     06/09/2012

##By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
##making use of the four arithmetic operations (+, , *, /) and
##brackets/parentheses, it is possible to form different positive integer
##targets.
##
##For example,
##
##8 = (4 * (1 + 3)) / 2
##14 = 4 * (3 + 1 / 2)
##19 = 4 * (2 + 3)  1
##36 = 3 * 4 * (2 + 1)
##
##Note that concatenations of the digits, like 12 + 34, are not allowed.
##
##Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
##target numbers of which 36 is the maximum, and each of the numbers 1 to 28
##can be obtained before encountering the first non-expressible number.
##
##Find the set of four distinct digits, a  b < c  d, for which the longest set
##of consecutive positive integers, 1 to n, can be obtained, giving your answer
##as a string: abcd.

from time import clock

def gettargets(w,x,y,z):
    targets = set()
    a = ((w + x) + y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) + y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) + y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) + y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) - y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) - y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) - y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) - y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) * y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) * y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) * y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) * y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) / y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) / y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) / y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w + x) / y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) + y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x + y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x + y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) + y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x + y) - z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x + y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) + y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x + y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x + y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) + y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x + y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x + y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) - y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x - y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x - y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) - y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x - y) - z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x - y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) - y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x - y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x - y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) - y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x - y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x - y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) * y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x * y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x * y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) * y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x * y) - z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x * y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) * y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x * y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x * y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) * y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x * y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x * y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) / y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x / y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x / y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) / y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x / y) - z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x / y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) / y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x / y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x / y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w - x) / y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w - ((x / y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w - (x / y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) + y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) + y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) + y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) + y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) - y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) - y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) - y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) - y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) * y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) * y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) * y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) * y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) / y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) / y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) / y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w * x) / y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) + y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x + y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x + y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) + y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    if x+y-z != 0:
        a = w / ((x + y) - z)
        if a%1 == 0 and a>0:
            targets.add(a)
    a = (w / (x + y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) + y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x + y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x + y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) + y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x + y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x + y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) - y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    if x-y+z != 0:
        a = w / ((x - y) + z)
        if a%1 == 0 and a>0:
            targets.add(a)
    a = (w / (x - y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) - y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    if x-y-z!=0:
        a = w / ((x - y) - z)
        if a%1 == 0 and a>0:
            targets.add(a)
    a = (w / (x - y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) - y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x - y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x - y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) - y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x - y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x - y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) * y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x * y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x * y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) * y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    if (x*y)-z != 0:
        a = w / ((x * y) - z)
        if a%1 == 0 and a>0:
            targets.add(a)
    a = (w / (x * y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) * y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x * y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x * y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) * y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x * y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x * y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) / y) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x / y) + z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x / y)) + z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) / y) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    if x/y-z!=0:
        a = w / ((x / y) - z)
        if a%1 == 0 and a>0:
            targets.add(a)
    a = (w / (x / y)) - z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) / y) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x / y) * z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x / y)) * z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = ((w / x) / y) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    a = w / ((x / y) / z)
    if a%1 == 0 and a>0:
        targets.add(a)
    a = (w / (x / y)) / z
    if a%1 == 0 and a>0:
        targets.add(a)
    return targets


maxsofar = 0


clock()
#pick 4 numbers
for a in range(1,7): #1 - 6
    for b in range(a+1,8):
        for c in range(b+1,9):
            for d in range(c+1,10):
                #print(a,b,c,d)
                picks = [a,b,c,d]
                targets = set()
                for n1 in picks:
                    for n2 in [x for x in picks if x != n1]:
                        for n3 in [x for x in picks if x not in [n1,n2]]:
                            for n4 in [x for x in picks if x not in [n1,n2,n3]]:
                                targets = targets.union(gettargets(n1,n2,n3,n4))
                for x in range(1,3024+1): #6*7*8*9
                    if x not in targets:
                        thismax = x-1
                        #print (thismax)
                        break
                if thismax > maxsofar:
                    maxsofar = thismax
                    print('max so far:', maxsofar, 'with numbers:',a,b,c,d)

print(clock(), 'seconds')

#need all orders of +,-,*,/

##ops = ['+','-','*','/']
##for o1 in ops:
##    for o2 in ops:
##        for o3 in ops:
##             print('    a = ((w',o1,'x)',o2,'y)',o3,'z')
##             print('    if a%1 == 0 and a>0:')
##             print('        targets.add(a)')
##             if o1 in ['-','/']:
##                 print('    a = w',o1,'((x',o2,'y)',o3,'z)')
##                 print('    if a%1 == 0 and a>0:')
##                 print('        targets.add(a)')
##                 print('    a = (w',o1,'(x',o2,'y))',o3,'z')
##                 print('    if a%1 == 0 and a>0:')
##                 print('        targets.add(a)')




##a=2
##b=3
##c=8
##d=9
##print(a,b,c,d)
##picks = [a,b,c,d]
##targets = set()
##for n1 in picks:
##    for n2 in [x for x in picks if x != n1]:
##        for n3 in [x for x in picks if x not in [n1,n2]]:
##            for n4 in [x for x in picks if x not in [n1,n2,n3]]:
##                targets = targets.union(gettargets(n1,n2,n3,n4))
##for x in range(1,3024+1): #6*7*8*9
##    if x not in targets:
##        thismax = x-1
##        print (thismax)
##        break
##if thismax > maxsofar:
##    maxsofar = thismax
##    print('max so far:', maxsofar, 'with numbers:',a,b,c,d)

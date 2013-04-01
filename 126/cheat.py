#-------------------------------------------------------------------------------
# Name:        126
# Purpose:
#
# Author:      uwi  http://wonderfl.net/c/cC40
#

from time import clock

def solve(M):
    ct = [0]*(M // 2)
    dsup = int(((M - 1) / 2)**.5)

    for d in range(dsup+1):
        p = 2 * d * (d - 1)
        asup = int((M / 2 - 2 * d * d - 1) / 2 / (d + 1))
        for a in range(1,asup+1):
            for b in range(1,a+1):
                for c in range(1,b+1):
                    v = a * b + b * c + c * a + 2 * d * (a + b + c) + p;  #key I missed... couldn't find the closed formula
                    if (v < M // 2):
                        ct[v]+=1
                    else:
                        break
    max = 0
    for i in range(M//2):
        if(ct[i] == 1000):
            print("1000!!",(i * 2))
        if(max < ct[i]):
            max = ct[i];
    return max;

clock()
print(solve(20000));
print(clock(),'seconds')

##        // L(a,b,c,d)=2(ab+bc+ca)+4(d-1)(a+b+c)+4(d-1)(d-2)
##        // d : depth
##        // C(n) = #{(a,b,c,d)|L(a,b,c,d)=n}

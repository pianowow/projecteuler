print('Author: pianowow')

from time import clock
from math import sqrt
from itertools import product
from itertools import permutations

prime = {2,3,5,7}
notprime = {1,4,6,8,9}

def is_prime(n):
    if n in prime:
        return True
    elif n in notprime:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        notprime.add(n)
        return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            notprime.add(n)
            return False
        else:
            f += 6
    prime.add(n)
    return True

def ninepandigitals():
    for lst in permutations(tuple(range(1,10))):
        if lst[-1] in {1,3,7,9}:
            yield lst

def combinedigits(digits):
    cntprimeset = 0
    for lst in product ((0,1), repeat=7):
        cblst = (0,)+lst+(1,)
        lastnum = 0
        num = digits[0]
        good = True
        for i in range(1,9):
            if cblst[i] == 1:
                num = num*10 + digits[i]
            else:
                if num > lastnum:
                    if is_prime(num):
                        lastnum = num
                        num = digits[i]
                    else:
                        good = False
                        break
                else:
                    good = False
                    break
        if good:
            if num > lastnum:
                if is_prime(num):
                    cntprimeset += 1
    return cntprimeset

clock()
cnt = 0
for digits in ninepandigitals():
    cnt += combinedigits(digits)

print(int(clock()), 'seconds')
print(cnt,'sets counted')

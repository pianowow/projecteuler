print('Author: Oyster, ke9tv')
print('translated to Python by pianowow')

from itertools import permutations, compress
from math import sqrt
from time import clock

DigitCount = 9
AllBits = (1 << DigitCount) - 1

_countsByBitmask = [0]*(AllBits + 1)
_reverseBitmasks = [0]*(AllBits + 1)

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

def GetNumber(digits):
    n = 0
    for digit in digits:
        n = n * 10 + digit
    return n

def CalculateMatchingPrimes():
    allDigits = list(range(1, DigitCount+1));
    for i in range(AllBits):
        digits = list(compress(allDigits, [i & (1<<j) for j,x in enumerate(allDigits)]))
        if (len(digits) == 1 or sum(digits) % 3 != 0):
            _countsByBitmask[i] = sum([1 for x in permutations(digits) if is_prime(GetNumber(x))])
            if (_countsByBitmask[i] != 0):
                reverseBitmasks = []
                for j in range(i+1,AllBits):
                    if ((i & j) == 0):
                        reverseBitmasks.append(j);
                _reverseBitmasks[i] = reverseBitmasks;

def CountAllSets(bits, bitmasks):
    if (bits == AllBits): return 1
    count = 0
    for i in bitmasks:
        if (bits & i == 0 and _countsByBitmask[i] != 0):
            count += _countsByBitmask[i] * CountAllSets(bits | i, _reverseBitmasks[i])
    return count

clock()
CalculateMatchingPrimes()
cnt = CountAllSets(0, list(range(1,AllBits+1)))
print(int(clock()), 'seconds')
print(cnt,'sets counted')
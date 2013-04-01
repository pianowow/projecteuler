print('Author: llevinson')
print('Translated to python and optimized by pianowow')

from itertools import permutations
from math import sqrt
from time import clock

cnt = 0

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

def findSetsRecursive(listOfNums):
  global cnt
  if (listOfNums) == []:
    digits = [1,2,3,4,5,6,7,8,9]
  else:
    notdigits = []
    for num in listOfNums:
        while num > 9:
            notdigits.append(num%10)
            num //=10
        notdigits.append(num)
    digits = [x for x in range(1,10) if x not in notdigits]

  if digits == []:
    cnt += 1
    return

  if listOfNums != []:
      for length in range(len(str(listOfNums[-1])),len(digits)+1):
        for numlst in permutations(digits,length):
            num = 0
            for i,digit in enumerate(numlst):
                num += digit*10**i
            if (num) > listOfNums[-1]:
                if is_prime(num):
                    newlistOfNums = listOfNums + [num]
                    findSetsRecursive(newlistOfNums)
                else:
                    continue
            else:
                continue
  else:
      for length in range(1,len(digits)+1):
        for numlst in permutations(digits,length):
            num = 0
            for i,digit in enumerate(numlst):
                num += digit*10**i
            if is_prime(num):
                newlistOfNums = listOfNums + [num]
                findSetsRecursive(newlistOfNums)
            else:
                continue

clock()
findSetsRecursive( [] )
print(int(clock()), 'seconds')
print(cnt,'sets counted')
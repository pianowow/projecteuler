#-------------------------------------------------------------------------------
# Name:        114
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
from time import clock

max = 50
cache = [-1]*(max+1)
cache[3] = 1

def count(gap, cache):
  if (gap < 3):
     return 0
  if (cache[gap] != -1):
     return cache[gap]

  total = 0
  for len in range(3,gap+1):
    total += gap - len + 1
    maxpos = gap - len + 1
    for pos in range(maxpos+1):
      total += count(gap - len - pos - 1, cache)
  cache[gap] = total
  return total

clock()
answer = 1 + count(max, cache)
print(clock(), 'seconds')
print(answer)

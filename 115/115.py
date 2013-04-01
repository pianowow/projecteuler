#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     06/09/2012

def count(m, gap, cache):
  if (gap < m):
     return 0
  if (cache[gap] != -1):
     return cache[gap]

  total = 0
  for len in range(m,gap+1):
    maxpos = gap - len + 1
    total += maxpos
    for pos in range(0,maxpos+1):
      total += count(m, gap - len - pos - 1, cache)
  cache[gap] = total
  return total

def F(m, n):
  cache = [-1]*(n+1)
  cache[m] = 1
  return 1 + count(m, n, cache)


BLOCK_LEN, LIMIT  =  50, 10**6

answer = BLOCK_LEN

while (F(BLOCK_LEN, answer) <= LIMIT):
  answer+=1

print (answer)

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/09/2012

##from itertools import count
##
##def resilience(d):
##    allpossible = list(range(1,d))
##    #for all divisors of d:
##    for div in [x for x in range(2,d//2+1) if d%x==0]:
##        #print('div:',div)
##        #remove all multiples of div from allpossible
##        for rem in [x for x in allpossible if x%div==0]:
##            #print('removing',rem)
##            allpossible.remove(rem)
##    #print(allpossible)
##    return len(allpossible)/(d-1)
##
###limit = 15499/94744
##limit = 2/10
##for d in count(2):
##    if resilience(d) < limit:
##        break
##print (d)


def gen_powers(powrange, maxlen, pows):
  if (len(pows) == maxlen):
    yield pows
  elif (len(pows) == 0):
    for it in powrange:
      for lst in gen_powers(powrange, maxlen, [it]):
        yield lst
  else:
    for it in [x for x in powrange if x>=pows[0]]:
      for lst in gen_powers(powrange, maxlen, [it]+pows):
        yield lst

POWER_RANGE = list(range(0,5))
answer =  1752002630070461520695765003094322410000+1
TARGET = 15499/94744
##TARGET = 4/10
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]

for powers in gen_powers(POWER_RANGE, len(primes), []):
  print(powers)
  d, factors =  1, []
  for i,v in enumerate(powers):
    if (v > 0):
        d *= primes[i] ** v
        factors.append(primes[i])

  if (d > 1):
    if (answer > d):
      totient = d
      for v in factors:
        totient *= (1-1/v)
      if totient/(d-1) < TARGET:
        answer = d
print (answer)



#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN

tries = 15

bluedraws = [0]*tries
reddraws = [0]*tries
totaldraws = [0]*tries

def binarystrings(n):
    if n == 1:
        for x in range(2):
            yield str(x)
    else:
        for x in range(2):
            for y in binarystrings(n-1):
                yield str(x)+y

blues = 1
reds = 1
for draw in range(tries):
    totaldraws[draw] = (blues+reds)
    reddraws[draw] = reds
    bluedraws[draw] = blues
    reds+=1

print (totaldraws)
print (reddraws)
print (bluedraws)

winprob = 0

outcomes = list(binarystrings(tries))


for i,outcome in enumerate(outcomes):
    prob = 1
    if outcome.count('1') > outcome.count('0'):
        for trie,draw in enumerate(outcome):
            if draw == '1':
                prob *= bluedraws[trie]/totaldraws[trie]
            else:
                prob *= reddraws[trie]/totaldraws[trie]
        winprob += prob

print(winprob)
print('payout:',int(1/winprob))
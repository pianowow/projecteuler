#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     06/09/2012

from csv import reader
from copy import copy


def sortstring(s):
    l = []
    for char in s:
        l.append(char)
    l.sort()
    ss = ''
    for char in l:
        ss += char
    return ss


def sortint(i):
    return sortstring(str(i))

def uniquedigits(n):
    s = str(n)
    alreadyseen = {}
    for char in s:
        if char in alreadyseen:
            alreadyseen[char] += 1
        else:
            alreadyseen[char] = 1
    for value in alreadyseen.values():
        if value > 1:
            return False
    return True

def reorder(n):
    map = {}
    key = 'BOARD'
    s = str(n)
    for i,digit in enumerate(s):
        map[key[i]] = digit
    other = 'BROAD'
    s = ''
    for char in other:
        s+=map[char]
    return int(s)

worddict = {}
wordpairs = []
maxwordlen = 0

file = reader(open('words.txt'))
for line in file:
    for word in line:
        n = len(word)
        if n > maxwordlen:
            maxwordlen = n
        sorted = sortstring(word)
        if sorted in worddict:
            wordpairs.append((worddict[sorted],word))
        else:
            worddict[sorted] = word

maxlen = 0
for a,b in wordpairs:
    if len(a) >= maxlen:
        print(a,b,len(a))
        maxlen = len(a)

print('maxwordlen:',maxwordlen)

numdict = {}
numpairs = []

for square in [x**2 for x in range(1,100000)]:
    if len(str(square)) > 6:
        break
    sorted = sortint(square)
    if sorted in numdict:
        numpairs.append((numdict[sorted],square))
    else:
        numdict[sorted] = square


candidates = []

for a,b in numpairs:
    la = len(str(a))
    lb = len(str(b))
    if la == 5:
        if uniquedigits(a):
            candidates.append(a)
            candidates.append(b)

print(len(candidates),'numbers:',candidates)

best = []

for x in candidates:
    y = reorder(x)
    #print(x,y)
    if y in candidates:
        best.append(x)
        best.append(y)

print(best)
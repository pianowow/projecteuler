#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     18/09/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from time import clock

doubles = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,50]

points = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','S14','S15','S16','S17','S18','S19','S20','S25',
'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20', 'D25',
'T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']

pointval = {
'S1': 1,'S2': 2,'S3': 3,'S4': 4,'S5': 5,'S6': 6,'S7': 7,'S8': 8,'S9': 9,'S10': 10,'S11': 11,
'S12': 12,'S13': 13,'S14': 14,'S15': 15,'S16': 16,'S17': 17,'S18': 18,'S19': 19,'S20': 20,'S25': 25,
'D1': 2,'D2': 4,'D3': 6,'D4': 8,'D5': 10,'D6': 12,'D7': 14,'D8': 16,'D9': 18,'D10': 20,'D11': 22,
'D12': 24,'D13': 26,'D14': 28,'D15': 30,'D16': 32,'D17': 34,'D18': 36,'D19': 38,'D20': 40,'D25': 50,
'T1': 3,'T2': 6,'T3': 9,'T4': 12,'T5': 15,'T6': 18,'T7': 21,'T8': 24,'T9': 27,'T10': 30,'T11': 33,
'T12': 36,'T13': 39,'T14': 42,'T15': 45,'T16': 48,'T17': 51,'T18': 54,'T19': 57,'T20': 60
}

checkouts = []

def pointtotal(initialdarts, double):
    ttl = double
    for dart in initialdarts:
        ttl += pointval[dart]
    return ttl

clock()

#three darts
for dart1 in points:
    for dart2 in points[points.index(dart1):]:
        first2 = [dart1, dart2]
        for dart3 in doubles:
            c = (first2,dart3)
            checkouts.append(c)

#two darts
for dart1 in points:
    for dart2 in doubles:
        c = ([dart1],dart2)
        checkouts.append(c)

#one dart
for dart1 in doubles:
    c = ([],dart1)
    checkouts.append(c)

cnt = 0
for initialdarts,double in checkouts:
    if pointtotal(initialdarts,double) < 100:
        cnt += 1

print(clock(), 'seconds')
print(cnt)
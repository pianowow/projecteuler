#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
from time import clock
def next_trib(n1,n2,n3):
    return n1+n2+n3

clock()
trie = 29
specialoddnums = [27]
trie = trie + 2
while len(specialoddnums) < 124:
    divides = False
    n1 = n2 = 1
    n3 = 3
    while True:
        n1,n2,n3 = n2,n3,next_trib(n1,n2,n3)%trie
        if n3 == 0:
            divides = True
            break
        if (n1==n2 and n2==n3):
            divides = False
            break
    if not divides:
        specialoddnums.append(trie)
        print (trie)
    trie += 2
print(clock(),'seconds')
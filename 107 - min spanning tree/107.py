#-------------------------------------------------------------------------------
# Name:        107
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     04/09/2012
from time import clock
clock()
from csv import reader
G = [] #graph from the file
file = reader(open('network.txt'))
for line in file: G.append([int(item.replace('-','0')) for item in line])
Gv = list(range(len(G))) #vertices in G
L = [set([x]) for x in Gv] #list of sets of vertices (merging these sets)
MST = [[0 for i in range(len(G))] for j in range(len(G))] #minimum spanning tree
while len(L) > 1:
    newL = []
    for T in L:
        min = 10000
        minv1 = -1
        minv2 = -1
        ##for each T in L, find the smallest edge connecting T to G-T
        for v1 in T:
            for v2 in [x for x in Gv if x not in T]:
                if G[v1][v2] > 0 and G[v1][v2] < min:
                    min = G[v1][v2]
                    minv1 = v1
                    minv2 = v2
        ##merge T with other T containing minv2
        for v2T in [x for x in L if minv2 in x]:
            newT = T.union(v2T)
            if newT not in newL:
                newL.append(newT)
                break
        ##add edge connecting minv1 and minv2 to MST
        MST[minv1][minv2] = G[minv1][minv2]
        MST[minv2][minv1] = G[minv2][minv1]
    L = newL
oldtotal = sum([x for row in G for x in row])/2
newtotal = sum([x for row in MST for x in row])/2
print(clock(),'seconds')
print('total savings',oldtotal-newtotal)

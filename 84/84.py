#-------------------------------------------------------------------------------
# Name:        84
# Purpose:     Attempting to solve ProjectEuler.net problem 84
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     27/08/2012
# Copyright:   (c) CHRISTOPHER_IRWIN 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from random import random
from copy import copy

def rolldice():
    return int(random()*6+1), int(random()*6+1)

board = list(range(40))
tries = 1000000
numDoubles = 0
currentSquare = 0 #start at Go

currentCommunityChest = 0 #which card to pick next
currentChance = 0

#throw the dice lots of times
for x in range(tries):
    roll1, roll2 = rolldice()

    if roll1 == roll2:
        numDoubles += 1
        if numDoubles == 3:
            currentSquare = 10
    else:
        numDoubles = 0
        currentSquare = (currentSquare + roll1 + roll2) %40

    #special rules for chance
    if currentSquare in (7, 22, 36):
        #draw a card
        if currentChance == 0: #advance to Go
            currentSquare = 0
        elif currentChance == 1: #go to jail
            currentSquare = 10
            numDoubles = 0
        elif currentChance == 2:
            currentSquare = 11
        elif currentChance == 3:
            currentSquare = 24
        elif currentChance == 4:
            currentSquare = 39
        elif currentChance == 5:
            currentSquare = 5
        elif currentChance in (6,7): #next railroad
            if currentSquare == 7:
                currentSquare = 15
            elif currentSquare == 22:
                currentSquare = 25
            elif currentSquare == 36:
                currentSquare = 5
        elif currentChance == 8: #next utility
            if currentSquare in (7,36):
                currentSquare = 12
            elif currentSquare == 22:
                currentSquare = 28
        elif currentChance == 9: #back 3 squares
            currentSquare -= 3
        #put it on the bottom
        currentChance = (currentChance + 1) % 16

    #special rules for community chest
    if currentSquare in (2, 17, 33):
        #draw a card
        if currentCommunityChest == 0: #advance to Go
            currentSquare = 0
        elif currentCommunityChest == 1: #go to jail
            currentSquare = 10
            numDoubles = 0
        #put it on the bottom
        currentCommunityChest = (currentCommunityChest + 1) % 16

    #special rule for go to jail square
    if currentSquare == 30:
        currentSquare = 10
        numDoubles = 0

    #record each square landing as an increment on board(currentSquare)
    board[currentSquare] += 1


boardcopy = copy(board)

best = max(boardcopy)
print ('1: '+str(best) + ' (square ' + str(board.index(best)) +')')
boardcopy.remove(best)

best = max(boardcopy)
print ('2: '+str(best) + ' (square ' + str(board.index(best)) +')')
boardcopy.remove(best)

best = max(boardcopy)
print ('3: '+str(best) + ' (square ' + str(board.index(best)) +')')
boardcopy.remove(best)
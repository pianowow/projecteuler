#-------------------------------------------------------------------------------
# Name:        126
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     06/12/2012


#The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.


#If we then add a second layer to this solid it would require forty-six cubes to cover every
#visible face, the third layer would require seventy-eight cubes, and the fourth layer would
#require one-hundred and eighteen cubes to cover every visible face.

#However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes;
#similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

#We shall define C(n) to represent the number of cuboids that contain n cubes in one
#of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

#It turns out that 154 is the least value of n for which C(n) = 10.

#Find the least value of n for which C(n) = 1000.
from time import clock

def record_layers(origx,origy,origz,maxlayer,histogram):
    #nextlayer = previouslayer + 1
    topandbottom = origx*origy*2
    middlelayercrosssections = [0]*(maxlayer+1)
    middlelayercrosssections[1]=origx*2 + origy*2
    successivelayers = [0]*(maxlayer+1)
    successivelayers[0] = origx*origy*origz #successivelayers[0] will be the original cubes themselves
    for x in range(1,maxlayer+1): #x is the number of layers of blocks on top of the original cuboid
        #print('working on layer',x)
        #corners on middle layer = (layer# - 1) * 4
        middlelayercrosssections[x] = origx*2 + origy*2 + (x-1)*4
        #need another for loop for adding all the middle layer cross sections up to this layer
        successivelayers[x] = middlelayercrosssections[x]*origz + topandbottom
        for y in range(1,x): #y is the previous layers added between the cuboid and current layer
            #print('y',y)
            #print(middlelayercrosssections[y]*2)
            successivelayers[x] += middlelayercrosssections[y]*2
        if successivelayers[x] not in histogram:
             histogram[successivelayers[x]] = [(origx,origy,origz,x)]
        else:
             histogram[successivelayers[x]].append((origx,origy,origz,x))
    return histogram

    #print (middlelayercrosssections)
    #print (successivelayers)
    #return successivelayers[nextlayer]


clock()
histogram = dict()
mx = 80
print('filling histogram for up to',mx,'layers of up to',str(mx)+'x'+str(mx)+'x'+str(mx),'size cuboids')

maxcubes = 0
for x in range(1,mx+1):
    for y in range(x,mx+1):
        for z in range(y,mx+1):
            record_layers(x,y,z,mx,histogram)
##                if cubecnt not in histogram:
##                    histogram[cubecnt] = [(x,y,z,layer)]
##                else:
##                    histogram[cubecnt].append((x,y,z,layer))

goal = 100
print('finding minimum cube layer size that has exactly',goal,'cuboids leading to it')
kys = list(histogram.keys())
kys.sort()
for x in kys:
    if x in histogram:
        if len(histogram[x]) == goal:
            print(x)
            break
print(clock(),'seconds')
print("max value from histogram:",max([len(x) for x in histogram.values()]))

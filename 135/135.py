#-------------------------------------------------------------------------------
# Name:        135
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     17/09/2012

#x**2 - y**2 - z**2 = n

#x > y > z



from time import clock


max = 50000000

#original version

##hist = [0]*max
##clock()
##for z in range(1,max+1):
##    k = z//3
##    x = z+2*k
##    y = z+k
##    n = x**2 - y**2 - z**2
##    while n < max:
##        if n > 0:
##            hist[n] += 1
##            #print (z,y,x,n,'k=',k)
##        k+=1
##        x = z+2*k
##        y = z+k
##        n = x**2 - y**2 - z**2
##
##cnt = 0
##
##for amt in hist:
##    if amt == 10:
##        cnt+=1
##
##print(clock(),'seconds')

#rewrite based on problem thread

#(p+q)^2 - p^2 - (p-q)^2 = n

#4pq - p^2 = n

#q = ( n + p^2 )/ 4p

#since p^2 = 0 mod p, n must also have a factor p.

#n = kp

#q = ( kp + p^2 ) / 4p

#q = ( k + p ) / 4

#the sum p + k must be divisible by 4. define a such that a+p = 0 mod 4

#k = 4v + a

#q = ( 4v + a + p )/ 4

#iterate
#for each p from 2 below the limit.
#for each v from 0 and while v < (3p-a)/4 and the candidate n = p( 4v+a ) < limit

#(record the hits)
hist = [0]*max
clock()
for p in range(2,max+1):
    a = 4-p%4
    for v in range(0,(3*p-a)//4):
        n = p*(4*v+a)
        if p*(4*v+a) >= max:
            break
        hist[n] += 1
cnt = 0
for amt in hist:
    if amt == 1:
        cnt+=1

print(clock(),'seconds')
print(cnt)
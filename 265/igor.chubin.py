#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      igor.chubin
#

def bin2dec(a):
    s=0
    for x in a: s=s*2+x
    return s

def check(a,l,n):
    r=[]
    for i in range(l):
        r+=[bin2dec(a[i:i+n])]
    return len(r)==len(set(r))

def gen(a,n):
    if len(a)==2**n:
        if check(a+a,len(a),n):
            return bin2dec(a)
    else:
        if check(a,len(a)-n+1,n):
            return gen(a+[0],n)+gen(a+[1],n)
    return 0

print (gen([0]*5,5))
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#


def u(k,r):
    return (900-3*k)*r**(k-1)

def s(r):
    n = 5000
    return sum([u(k,r) for k in range(1,n+1)])

def find_next_num(num):
    candidate = 0
    for digit in range(10):
        candidate_next = num+digit/10**(len(str(num))-1)
        result = s(candidate_next)
        if (result > -600000000000):
            candidate = candidate_next
        else:
            break
    print(candidate, result)




#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/09/2012

from math import sqrt

def GeneratePrimes(limit):
    RetValue = {2,3}
    Stepper = 5
    Check = 1
    while (Stepper <= limit):

        for i in RetValue:

            if (Stepper % i == 0):
                Check = 0
                break
            if sqrt(Stepper) < i:
                break

        if (Check == 1):
            #//Console.WriteLine(((float)Stepper / (float)limit) * 100);
            RetValue.add(Stepper)

        Check = 1
        Stepper+=2

    return RetValue

primes = GeneratePrimes(1000);
count = 0;
i = 1
check = 1
while check < 1000000:
    check = ((i+1)*(i+1)*(i+1)) - (i*i*i);
    prime = True
    for p in [x for x in primes if x<check]:
        if ((check % p) == 0):
            prime = False
            break
    if prime:
        count += 1
    i+=1

print(count)

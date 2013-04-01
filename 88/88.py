#-------------------------------------------------------------------------------
# Name:        88
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/09/2012

##SIZE = 12000;
##
##RANGE = 24000; #P.S. RANGE can be smaller, down to 12,200
SIZE = 6;

RANGE = 12; #P.S. RANGE can be smaller, down to 12,200


k = [0]*(SIZE + 1)

nums = [0]*(RANGE + 1)

for i in range(RANGE+1):
    nums[i] = set()



#dynamically calculate all the k's

for i in range(2,int(RANGE/2)+1):

    nums[i].add(-i + 1)


    for num in nums[i]:
        current = i + i;
        new_num = num - 1;
        #for (int j = 2; j <= i && current <= RANGE; j++) {
        j = 2
        while j <= i and current <= RANGE:
            nums[current].add(new_num);
            pk = current + new_num;
            if (pk <= SIZE and (current < k[pk] or k[pk] == 0)):
                 k[pk] = current;
            new_num-=1;
            current += i;
            j+=1





#show the answer

success = True;

for i in range(2,len(k)):
    if (k[i] == 0):
        success = False

if (success):
    #k = ArraysUtils.sortAndRemoveDuplicates(k)
    kset = set(k)
    sum = 0
    for i in kset:
         sum += i
    print(sum)


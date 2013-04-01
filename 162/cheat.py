#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
##from string import upper

digits=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def f2(cache, have_0=False, have_1=False, have_A=False, have_something_in_front=False, remain=0):

    fn_params=(have_0, have_1, have_A, have_something_in_front, remain)
    if fn_params in cache:
        return cache[fn_params]

    if remain==0:
       if have_0 and have_1 and have_A:
           return 1
       else:
           return 0
    else:
       rt=0
       for d in digits:
           rt = rt + f2 (cache,
                         have_0 or ('0' in d and have_something_in_front),
                         have_1 or ('1' in d),
                         have_A or ('A' in d),
                         have_something_in_front or (d != '0'),
                         remain-1)

       cache[fn_params]=rt
       return rt
cache = {}
print (hex(f2(cache, remain=16)).upper())
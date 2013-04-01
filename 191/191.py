#-------------------------------------------------------------------------------
# Name:        191
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     10/09/2012

##A particular school offers cash rewards to children with good attendance and
##punctuality. If they are absent for three consecutive days or late on more
##than one occasion then they forfeit their prize.
##
##During an n-day period a trinary string is formed for each child consisting
##of L's (late), O's (on time), and A's (absent).
##
##Although there are eighty-one trinary strings for a 4-day period that can be
##formed, exactly forty-three strings would lead to a prize:
##
##OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
##OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
##AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
##AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
##LAOO LAOA LAAO
##
##How many "prize" strings exist over a 30-day period?

### [n, tot, -AA, 0Ls, -A, 1L-AA, 1L-A, 1LnotA]
##lst = [1, 3, 0, 2, 1, 0, 0, 1]
##while lst[0] < 30:
##  n, t, a, b, c, d, e, f = lst
##  lst = [n + 1, 2 * t + b - a, c, 2 * b - a + d, t - (a + c), e, f, t]
##
##print( lst[1]) # => 1918080160


#@memo
def f(n, a, l):
    if n == 0:
        return 1
    # 'O'
    ret = f(n - 1, 0, l)
    # 'L'
    if l == 0:
        ret += f(n - 1, 0, 1)
    # 'A'
    if a < 2:
        ret += f(n - 1, a + 1, l)
    return ret

print (f(30, 0, 0))
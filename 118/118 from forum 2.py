print('Author: Francky')

from itertools import permutations
from math import sqrt
from time import clock

def PE118():
  prime = {2,3,5,7}
  pasprime = {1,4,6,8,9}
  def is_prime(n):
    if n in prime:
        return True
    elif n in pasprime:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        pasprime.add(n)
        return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            pasprime.add(n)
            return False
        else:
            f += 6
    prime.add(n)
    return True

  # on prend les permutations de 123456789,
  # on y place des barrières pour partitionner.
  # n barrières => n+1 nombres
  res=0
  for x in permutations([1,2,3,4,5,6,7,8,9], 9):
   if x[-1] not in {2,4,5,6,8}:
    # Zéro barrière ; un seul nombre => pas premier, somme des chiffres = 45 ; divi par 3
    #----------------
    # Deux nombres ; une barrière : b1 entre 1 et 4
    # a bcdefghi à abcd efghi
    for b1 in range(1,5):
      n1=x[:b1]
      if sum(n1)%3 or n1==(3,):
        p1 = 0
        for c in n1: p1 = 10*p1 + c
        if is_prime(p1):
          n2=x[b1:]
          if sum(n2)%3:
            p2 = 0
            for c in n2: p2 = 10*p2 + c
            if is_prime(p2): res+=1
          # maintenant, on va couper n2 en deux ; deux barrières ; trois nombres
          for b2 in range(b1, 1+(9-b1)//2): #1 1 7 à 3 3 3, en passant par 1 4 5
            n2=x[b1:b1+b2]
            if sum(n2)%3 or n2==(3,): # c'est le dernier cas où n==3 est possible
              p2 = 0
              for c in n2: p2 = 10*p2 + c
              if p1<p2 and is_prime(p2):
                n3=x[b1+b2:]
                if sum(n3)%3:
                  p3 = 0
                  for c in n3: p3 = 10*p3 + c

                  if p2<p3 and is_prime(p3): res+=1
                # maintenant, on va couper n3 en deux ; trois barrières ; 4 nombres
                for b3 in range(b2, 1+(9-b1-b2)//2): # 1 1 1 6 à 2 2 2 3, en passant par 1 1 3 4
                  n3=x[b1+b2:b1+b2+b3]
                  if sum(n3)%3: # n3=3 est impossible
                    p3 = 0
                    for c in n3: p3 = 10*p3 + c

                    if p2<p3 and is_prime(p3):
                      n4=x[b1+b2+b3:]
                      if sum(n4)%3:
                        p4 = 0
                        for c in n4: p4 = 10*p4 + c

                        if p3<p4 and is_prime(p4): res+=1
                      # maintenant, on va couper n4 en deux ; quatre barrières ; 5 nombres
                      for b4 in range(b3, 1+(9-b1-b2-b3)//2):
                        n4=x[b1+b2+b3:b1+b2+b3+b4]
                        if sum(n4)%3:
                          p4 = 0
                          for c in n4: p4 = 10*p4 + c
                          if p3<p4 and is_prime(p4):
                            n5=x[b1+b2+b3+b4:]
                            if sum(n5)%3:
                              p5 = 0
                              for c in n5: p5 = 10*p5 + c

                              if p4<p5 and is_prime(p5): res+=1
  # on a traité 0,1,2,3,4 barrières !!!
  #----------------------------------
  # il n'y a que 2,3,5,7 qui soient premiers.
  # Plus de 5 barrières => il y aura des composés !!!
  #---------------------------------------
  # 5 barrières (6 nombres).
  # Cas 1 : 1 1 1 1 2 3
  # Cas 2 : 1 1 1 2 2 2
  #-------+++++++------
  # Cas 1 : Il y 2,3,5,7 d'un côté,
  # il reste 1 et 9 avec 4,6,8 à partager en 2 premiers.
  # A]**1, *9 ou B]*1, **9
  # A] seul 89 est possible, il reste 4 et 6
  res+=is_prime(461)+is_prime(641) # double bingo !!
  # B] seuls 41, 61 sont possibles
  # 41, il reste 6,8 pour 9
  res+=is_prime(689)+is_prime(869) # plouf
  # 61, il reste 4,8 pour 9
  res+=is_prime(481)+is_prime(841) # plouf
  # Cas 2 : 1 1 1 2 2 2
  # On prend un parmi 2,3,5,7
  # que l'on ajoute à 1,4,6,8,9 à couper en trois de deux chiffres.
  # ab cd ef (avec a<c<e pour les compter qu'une fois)
  for p in [2,3,5,7]:
    for a,b,c,d,e,f in permutations([p,1,4,6,8,9], 6):
      if a<c and c<e and (a+b)%3 and (c+d)%3 and (e+f)%3 and \
        is_prime(10*a+b) and is_prime(10*c+d) and is_prime(10*e+f):
          res+=1
  return res

clock()
num = PE118()
print(int(clock()), 'seconds')
print (num,'sets counted')
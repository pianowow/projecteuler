
########################################################################
#   Common functions used for solving projectEuler.net. problems.
#   Copyright (C) 2011  Santiago Alessandri
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   You can contact me at san.lt.ss@gmail.com
#   Visit my wiki at http://wiki.san-ss.com.ar
########################################################################

from math import sqrt

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def rho(set):
    resultSet = [[]]
    for elem in set:
        tmpResultSet = (list(x) for x in resultSet)
        for newSet in tmpResultSet:
            newSet.append(elem)
        resultSet += tmpResultSet
    return resultSet

def sum_of_consecutive_squares(base, top):
    result = 0
    if base == 0:
        result += 1
    result += (top * (top + 1) * (2 * top + 1)) // 6
    result -= ((base - 1) * base * (2 * (base - 1) + 1)) // 6
    return result

def is_palindrome(x):
    x = str(x)
    for i in range(0, len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True

def gcd(a, b):

    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    if b == 0: return a
    while b != 0:
        (a, b) = (b, a % b)
    return a

def mcm(a, b):
    return a * b // gcd(a, b)


def is_square(n):
    return int(n ** (0.5)) ** 2 == n

def is_prime(number):
    if number == 2:
        return True
    if number & 1 == 0:
        return False
    i = 3
    limit = int(number ** (0.5))
    while i <= limit:
        if (number % i) == 0:
            return False
        i += 2
    return True

def find_primes_less_than(n):
    not_p = set()
    primes = []
    for i in range(2, n):
        if i not in not_p:
            primes.append(i)
            for j in range(i * 2, n, i):
                not_p.add(j)
    return primes

def phi(n):
    result = n
    i = 2

    while i ** 2 <= n:
        if n % i == 0:
            result -= result // i
        while n % i == 0:
            n //= i
        i += 1
    if n > 1:
        result -= result // n
    return result

def is_pandigital(x):
    str_x = str(x)
    if len(str_x) != 9:
        return False
    digits_set = set(str_x.replace('0', ''))
    return len(digits_set) == 9

def is_permutation(x, y):

    digits_x = {}
    for d in str(x):
        digits_x[d] = digits_x.get(d, 0) + 1

    digits_y = {}
    for d in str(y):
        digits_y[d] = digits_y.get(d, 0) + 1

    return digits_x == digits_y

def factors(n):
    result = set()
    sq = int(n ** (0.5))
    for x in range(1, sq + 1):
        if n % x == 0:
            result.add(x)
            result.add(n / x)
    if sq ** 2 == n:
        result.add(sq)
    return result

def solve_cuadratic(a, b, c):
    inner_root = b ** 2 - 4 * a * c
    if inner_root < 0:
        return None
    sqrt_inner_root = inner_root ** (0.5)
    return ((-b - sqrt_inner_root) / (2 * a), (-b + sqrt_inner_root) / (2 * a))

def mod_pow(base, exp, mod):
    res = 1
    while exp > 0:
        if exp & 1:
            res = (res * base) % mod
        exp >>= 1
        base = (base ** 2) % mod
    return res

# https://www.codewars.com/kata/5742e725f81ca04d64000c11

# Check if given numbers are prime numbers.
# If number N is prime return "Probable Prime" else  return "Composite".
#
# HINT: Upper bount is really big so you should use an efficient algorithm.
#
# Input
#   1 < N ≤ 10^100
#
# Example
#   prime_or_composite(2) # should return Probable Prime
#   prime_or_composite(200) # should return Composite

import random

def prime_or_composite(n):
    return 'Probable Prime' if miller_rabin(n) else 'Composite'

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

import random
import math

""" Valemiga
"""
# https://geekflare.com/prime-number-in-python/

def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

""" Eratosthenes
"""
# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            print(p)

""" Fermat
"""
# https://code-maven.com/fermat-primality-test

def get_coprime(n):
    while True:
        coprime = random.randrange(n)
        if math.gcd(coprime, n) == 1:
            return coprime

def fermat_primality(n, count = 1):
    for _ in range(count):
        a = get_coprime(n)
        if (a ** (n-1)) % n != 1:
            return False
    return True

n = int(input("Sisesta number: "))
print(f'Valem: {is_prime(n)}')
print(f'Algarvud kuni arvuni {n} (Eratosthenes):')
SieveOfEratosthenes(n)
print(f'Fermat: {fermat_primality(n)}')
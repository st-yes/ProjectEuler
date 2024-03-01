from math import sqrt
def isPrime(n):
    i = 2
    maxDiv = sqrt(n) #stop at the square root instead of division
    if n < 2:
        return False
    while (i <= maxDiv):
        if (n % i == 0):
            return False
        i += 1
    return True

def findPrime(n):
    i = 2
    n_prime = 0
    while (True):
        if isPrime(i):
            n_prime += 1
            if (n_prime == n):
               return i
        i += 1
# print(isPrime(4))
print(findPrime(10001))
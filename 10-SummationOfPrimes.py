from math import sqrt
def isPrime(n):
    i = 2
    maxDiv = sqrt(n)
    if n < 2:
        return False
    while (i <= maxDiv):
        if (n % i == 0):
            return False
        i += 1
    return True


def sumOfPrimesBellow(n):
    i = 2
    the_sum = 0
    while (i < n):
        if (isPrime(i)):
            the_sum += i
        i += 1
    return (the_sum)

print(sumOfPrimesBellow(2000000))
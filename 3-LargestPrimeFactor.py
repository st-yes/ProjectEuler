# What is the largest prime factor of the number 600851475143

def isPrime(n):
    i = 2
    maxDiv = n // 2
    if n < 2:
        return False
    while (i <= maxDiv):
        if (n % i == 0):
            return False
        i += 1
    return True

def primeFactor(n):
    i = 2
    while (n > 1):
        if (isPrime(i) and n % i == 0):
            n = n // i
        else:
            i += 1
    return (i) #last prime factor == biggest

if (__name__ == "__main__"):
    num = 600851475143
    print(f"biggest prime factor is {primeFactor(num)}")
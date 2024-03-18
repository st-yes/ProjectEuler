from math import sqrt


def findDivisor(n):
    max_div = sqrt(n)
    i = 2
    count = 2 #there is always at least 2 divisors: 1 and the number itself (except for 1)
    while (i <= max_div):
        if (n % i == 0):
            count += 2 # for i and n // i
        i += 1
    return count



def generateTriangleNumbers():
    i = 1
    tri_num = 1000
    while (True):
        tri_num = (i * (i + 1)) // 2
        if (findDivisor(tri_num) > 500):
            return tri_num
        i += 1

print(generateTriangleNumbers()) #76576500
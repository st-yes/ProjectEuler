# first generate Pythagorean triplet
from math import sqrt
# formula for generating pythagorean triples
# given an arbitrary pair of integer m and n, such as m > n > 0
# a**2 + b**2 = c**2
# then  a = m**2 - n**2 
# and b = 2mn
# and c = m**2 + n**2

# 1 2       
# 1 3   1 
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10

def generatePythagorean():
    n = 1
    m = 2
    while m < 50: #50 is arbitrary
        n = 1
        while (n < m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if (a + b + c == 1000):
                return ((a, b, c), a * b * c)
            n += 1
        m += 1
      
print (f"the triplets = {generatePythagorean()[0]}, their product = {generatePythagorean()[1]}")  #(375, 200, 425),  31875000
        
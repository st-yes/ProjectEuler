#Find the sum of the even-valued terms.
def generateFibo(n):
    firstTerm, secondTerm = 0, 1
    value, theSum = 0, 0
    while (value < n):
        value = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = value
        theSum += value if value % 2 == 0 else 0
    print(f"the sum = {theSum}")


if (__name__ == "__main__"):
    generateFibo(4000000) #4613732

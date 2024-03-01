## first let's find 2020

def find_smallest(n):
    i = 1
    small = n
    while(True):
        # if small % n == 0
        i = n
        while  i >= 1 and small % i == 0:
            i -= 1
        if (i != 0):
            small += 1
        else:
            break
    return(small)
    
print(find_smallest(20)) #232792560
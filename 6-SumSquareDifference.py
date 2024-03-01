
def sum_of_squares(n):
    i = 1
    the_sum = 0
    while (i < n + 1):
        the_sum += i **2
        i += 1
    return the_sum

def square_of_sum(n):
    return sum(list(range(1, n + 1))) ** 2
    
print(square_of_sum(100) - sum_of_squares(100)) #25164150
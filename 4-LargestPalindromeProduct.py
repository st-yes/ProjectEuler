# The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 * 99

# Find the largest palindrome made from the product of two 
# 3-digit numbers.

def isPalindrome(num):
    num = str(num)
    return True if num == num[::-1] else False

def largestPalindrome():
    num1 = 999
    num2 = 999
    result = 0
    max_palindrome = 0 #instead of list for a space complexity of (1)
    while (num1 >= 100):
        num2 = 999
        while (num2 >= 100):
            result = num1 * num2
            if (isPalindrome(result) == True):
                if result > max_palindrome:
                    max_palindrome = result
            num2 -= 1
        num1 -= 1
    return max_palindrome

print(largestPalindrome()) #906609
# 9. Generate a list of four digit numbers in a given range with all their digits even and the
# number is a perfect square.

from math import sqrt

def isAllEven(number):
    evenList = [0,2,4,6,8] #stores all even numbers so we can easily check if any of the digits in the number belongs to this even number list
    while number > 0:
        endNo = number%10 # When divided by 10 we always get the end number as remainder: Example 19 mod 10 = 9 and 10 mod 10 = 0. We can use this logic to get the last numbers in each iteration
        if endNo not in evenList: # This condition checks if we come across any odd digits in the number. In that case we don't need to check further. Since even having 1 odd digit in the given number makes it invalid for our program.
            return False
        number = number // 10 # using //10 on any number with remove the last digit from it. For example: 10//10 =1 or 100//10 = 10. 199//10 = 19. "//" removes if there are any decimal points in the numbers
    return True

def isPerfectSquare(number):
    srt = int(sqrt(number)) #sqrt method gives us the square root of a number
    if srt * srt == number: 
        return True
    else:
        return False



def fourDigitGenerator():
    start = int(input("Enter the starting range of the list: "))
    end = int(input("Enter the ending range of the list: "))
    if not start>999 or not end<10000:
        print("Enter a starting and ending range that is within the 1000 to 9999 range: ")
        fourDigitGenerator()
    for number in range(start,end+1):
        if isAllEven(number):
            if isPerfectSquare(number):
                print(number)

        
fourDigitGenerator() #function that generates the random 4 digit numbers

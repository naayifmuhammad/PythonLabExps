# 2. Write a function in file Armstrong.py to check whether a number is an Armstrong number.
# Import the module to generate Armstrong numbers between two limits.

def armstrongNumber(number):
    numStr = str(number)
    power = len(numStr)
    
    sumOfPowers = 0
    for digit in numStr:
        sumOfPowers+=int(digit)**power
    if number == sumOfPowers:
        return True
    else:
        return False

while(True):
    if armstrongNumber(int(input("Enter a number: "))):
        print(f"It is an armstrong number")
    else:
        print(f"It is not an armstrong number")


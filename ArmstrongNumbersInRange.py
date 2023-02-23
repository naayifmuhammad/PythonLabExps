# 2. Write a function in file Armstrong.py to check whether a number is an Armstrong number.
# Import the module to generate Armstrong numbers between two limits.

from armstrong import armstrongNumber

def armstrongInRange(starting,ending):
    print(f"Armstrong numbers in range of {starting} and {ending} are: ")
    for number in range(starting,ending+1):
        if armstrongNumber(number):
            print(number)

starting = int(input("Enter the starting range: "))
ending = int(input("Enter the ending range: \n"))
armstrongInRange(starting,ending)
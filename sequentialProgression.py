# 7. Write a program to sum the series 1/1! + 4/2! + 27/3! + ..... + nth term.

def factorial(number):
    factorial=1
    while number>0:
        factorial *=number
        number-=1
    return factorial

def printSeries(n):
    sum =0
    for i in range(1,n+1):
        sum+=i**i/factorial(i)
    return sum

n = int(input("Enter the length of series"))
print("Sum of n terms of this series is: ",printSeries(n))



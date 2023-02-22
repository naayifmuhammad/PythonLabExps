# 1. Write a Python function called ‘compare’ which takes two strings S1, S2 and an integer n as
# arguments. The function should return True if the first n characters of both the strings are
# the same else the function should return False.

def compare(s1,s2,n):
    if(s1[:n] == s2[:n]):
        return True
    else:
        return False

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
n = int(input("Enter the length property for comparison: "))
if compare(s1,s2,n):
    print(f"First {n} characters of {s1} and {s2} are same")
else:
    print(f"First {n} characters of {s1} and {s2} are not same")


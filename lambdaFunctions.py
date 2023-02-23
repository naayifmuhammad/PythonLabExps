# Write lambda functions to find the area of square, rectangle and triangle.
import math

areaRectangle = lambda a,b: a*b
areaCircle = lambda r: math.pi * r* r
areaTriangle = lambda b,h : 1/2 * b * h

area = areaRectangle(int(input("Enter the length")),int(input("Enter the breadth")))
print("Area of rectangle = ",area)
area = areaCircle(int(input("Enter radius")))
print(f"Area of Circle = {area}")
area = areaTriangle(int(input("Enter the length")),int(input("Enter the breadth")))
print("Area of triangle = ",area)
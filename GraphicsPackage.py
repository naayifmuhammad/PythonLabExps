# 10.Create a package graphics with modules rectangle, circle and sub-package 3D-graphics
# with modules cuboid and sphere. Include methods to find area and perimeter of respective
# figures in each module. Write programs that find the area and perimeter of figures by
# different importing statements.

from graphics.rectangle import *
from graphics.circle import *
from graphics.graphics3D import cuboid
from graphics.graphics3D import sphere

def operations():
    ch = int(input("\nSelect a shape to calculate it's Area and Perimeter/Circumference?\n0. Exit 1.Rectangle 2.Circle 3.Cuboid 4.Sphere: "))
    if ch == 1:
        length = int(input("Length? "))
        breadth = int(input("Breadth? "))
        print("Area = {:.2f}".format(rectangle_area(length, breadth)))
        print("Perimeter = {:.2f}".format(rectangle_perimeter(length,breadth)))
    elif ch == 2:
        radius = int(input("Radius? "))
        print("Area = {:.2f}".format(circle_area(radius)))
        print("Perimeter = {:.2f}".format(circle_circumference(radius)))
    elif ch == 3:
        length = int(input("Length? "))
        breadth = int(input("Breadth? "))
        height = int(input("Height? "))
        print("Area = {:.2f}".format(cuboid.cuboid_surface_area(length,breadth,height)))
        print("Perimeter = {:.2f}".format(cuboid.cuboid_perimeter(length,breadth,height)))
    elif ch == 4:
        radius = int(input("Radius? "))
        print("Area = {:.2f}".format(sphere.sphere_surface_area(radius)))
        print("Perimeter = {:.2f}".format(sphere.sphere_circumference(radius)))
    elif ch == 0:
        return
    operations()

operations()
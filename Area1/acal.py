# Write a program to calculate the area of any 2D shape.
import math
print(
    " Enter a shape from the following:\n [Circle, Rectangle, Triangle, Square, Rhombus, Trapezoid]\n")
shape = input("Shape? ")

if shape.lower() == "circle":
    r = float(input("Radius: "))
    area = math.pi * pow(r, 2)
    print(
        f"Area = 3.14 x r^2 \n      =3.14 x {r}^2\n     = 3.14 x {pow(r,2)}\n       = {round(area,2)}")
elif shape.lower() == "rectangle":
    l = float(input("Lenght: "))
    w = float(input("width: "))
    area = l * w
    print(f"Area = L x W\n      = {l} x {w}\n       = {area}")
elif shape.lower() == "triangle":
    b = float(input("Base: "))
    h = float(input("height: "))
    area = (b * h) / 2
    print(
        f"Area = (b x h)/2\n      = ({b} x {h})/2\n       = {(b*h)}/2\n       ={area}")
elif shape.lower() == "square":
    l = float(input("length: "))
    area = pow(l, 2)
    print(f"Area = l^2\n        ={l}^2\n        = {area}")
elif shape.lower() == "rhombus":
    d1 = float(input("Diagonal 1: "))
    d2 = float(input("Diagonal 2: "))
    area = (d1 * d2)
    print(f"Area = (d1 x d2)\n      = {d1} x {d2}/n     = {area}")
elif shape.lower() == "Trapezoid":
    b1 = float(input("base_1 "))
    b2 = float(input("base_2 "))
    h = float(input("height "))
    area = (b1 + b2) * h/2
    print(
        f"Area = (b1 + b2) x h/2\n        = ({b1} + {b2}) x {h}/2\n       = {b1*b2} x {h/2}\n     = {area}")
else:
    print("I don't have data on that shape yet")


import math

def factorial_calc():
    n = int(input("Enter a number: "))
    print(f"Factorial: {math.factorial(n)}")

def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = float(input("Enter time (in years): "))
    amount = p * (1 + r/100) ** t
    print(f"Compound Interest: {amount:.2f}")
    print(f"Interest only: {amount - p:.2f}")

def trigonometry():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print(f"sin({angle}) = {math.sin(rad):.4f}")
    print(f"cos({angle}) = {math.cos(rad):.4f}")
    print(f"tan({angle}) = {math.tan(rad):.4f}")
    print(f"sqrt({angle}) = {math.sqrt(angle):.4f}")
    print(f"log({angle}) = {math.log(angle):.4f}")

def area_shapes():
    print("1. Circle  2. Rectangle  3. Triangle")
    ch = input("Enter choice: ")
    if ch == "1":
        r = float(input("Enter radius: "))
        print(f"Area of Circle: {math.pi * r * r:.2f}")
    elif ch == "2":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print(f"Area of Rectangle: {l * b:.2f}")
    elif ch == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area of Triangle: {0.5 * b * h:.2f}")
    else:
        print(" choice!")

def menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        ch = input("Enter your choice: ")
        if ch == "1": factorial_calc()
        elif ch == "2": compound_interest()
        elif ch == "3": trigonometry()
        elif ch == "4": area_shapes()
        elif ch == "5": break
        else: print("choice!")
'''
TPRG 2131 Fall 2025 Assignment 1
Sept, 2025
Seb A <sebastian.azevedo@durhamcollege>

Built from project template.

*********
A/V calculator:

second attempt. This solution is all original with time no help from A.I. 

'''





#import important stuff
import math

#functions definitions


def get_positive_value(message):
    value = float(input(message))
    while value <= 0.0:
        value = float(input("The value must be greater than zero\n"
+ message))
    return value
 #functions for each calculation      
def area_rectangle(a,b):
    area = a*b
    return area

def area_circle(r):
    area = math.pi*(r**2)
    return area

def area_triangle(b,h):
    area = b*h*0.5
    return area

def volume_sphere(r):
    vol = (4/3)*math.pi*(r**3)
    return vol

def volume_cube(s):
    vol = s**3
    return vol
#mainguard 
if __name__ == '__main__':
    # initialize mode variable to allow two different behaviors later
    mode = 1

    # actual calculation loop:
    while True:
        print("Calculator is in Mode", mode, "\n")
        operation = builtins.input("Select Operation:\n1. area of a rectangle\n2. area of circle\n3. area of triangle\n4. volume of sphere\n5. volume of cube\n")

        try:
            if operation == "1":
                a = get_positive_value("what is L?")
                b = get_positive_value("What is H?")
                area = area_rectangle(a, b)
                if mode == 1:
                    print("the area of this rectanguloid is:", area)
                elif mode == 2:
                    print(a, "*", b, "=", area)

            elif operation == "2":
                r = get_positive_value("what is the radius?")
                area = area_circle(r)
                if mode == 1:
                    print("the area of this circle is:", area)
                elif mode == 2:
                    print("pi*", r, "^ 2 = ", area)

            elif operation == "3":
                b = get_positive_value("what is B?")
                h = get_positive_value("What is H?")
                area = area_triangle(b, h)
                if mode == 1:
                    print("the area of this triangle is:", area)
                elif mode == 2:
                    print("0.5*", b, "*", h, " = ", area)

            elif operation == "4":
                r = get_positive_value("what is the Radius?")
                volume = volume_sphere(r)
                if mode == 1:
                    print("the volume of this sphere is:", volume)
                elif mode == 2:
                    print("(4/3)pi", r, "^ 3 = ", volume)

            elif operation == "5":
                s = get_positive_value("what is the sidelength?")
                volume = volume_cube(s)
                if mode == 1:
                    print("the volume of this cube is:", volume)
                elif mode == 2:
                    print(s, "^ 3 = ", volume)

            # supplementary conditions: changing the mode or quitting etc.

            # quitting conditions
            elif operation == "q" or operation == "Q":
                break
            
            # toggle the mode
            elif operation == "v" or operation == "V":
                mode = 2 if mode == 1 else 1
            
            # reset to default
            elif operation == "d" or operation == "D":
                mode = 1

            else:
                print("try a different number, jerk!\n")
        # attempt to catch all other conditions
        except ValueError:
            print("try a different number, jerk!\n")




'''
TPRG 2131 Fall 2025 Assignment 1
Sept, 2025
Seb A <sebastian.azevedo@durhamcollege>

Built from project template.

Google gemini was used to help to implement the different view modes after much unsuccessful tinkering.
it also "cleaned up" quite a few other things, and added fancy bracers all over the place, without being asked.

*********
'''


#import important stuff
import math


# Define constants for the two view modes
VIEW_DEFAULT = 'default'
VIEW_CALCULATION = 'calculation'

# Set the initial view mode
current_view = VIEW_DEFAULT

#functions definitions

def get_positive_value(message):
    """Prompts the user for a numeric value and ensures it's positive."""
    while True:
        try:
            value = float(input(message))
            if value > 0.0:
                return value
            else:
                print("The value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def area_rectangle(a, b):
    """Calculates the area of a rectangle and returns the result and calculation string."""
    area = a * b
    calculation = f"A * B = {a} * {b}"
    return area, calculation

def area_circle(r):
    """Calculates the area of a circle (Area = pi * r^2) and returns the result and calculation string."""
    area = math.pi * (r ** 2)
    calculation = f"pi * r^2 = {math.pi:.4f} * ({r}^2)"
    return area, calculation

def area_triangle(b, h):
    """Calculates the area of a triangle (Area = 0.5 * base * height) and returns the result and calculation string."""
    area = b * h * 0.5
    calculation = f"0.5 * B * H = 0.5 * {b} * {h}"
    return area, calculation

def volume_sphere(r):
    """Calculates the volume of a sphere (Volume = (4/3) * pi * r^3) and returns the result and calculation string."""
    vol = (4/3) * math.pi * (r ** 3)
    calculation = f"(4/3) * pi * r^3 = 1.3333 * {math.pi:.4f} * ({r}^3)"
    return vol, calculation

def volume_cube(s):
    """Calculates the volume of a cube (Volume = s^3) and returns the result and calculation string."""
    vol = s ** 3
    calculation = f"s^3 = {s}^3"
    return vol, calculation


#actual loop:

while True:
    #print(f"--- Current View: {current_view.upper()} ---")
    operation = input(
        "Select Operation:\n"
        "1. area of a rectangle\n"
        "2. area of circle\n"
        "3. area of triangle\n"
        "4. volume of sphere\n"
        "5. volume of cube\n"
    ).lower()

    # 1. Handle Quit Command (Q/q)
    if operation == "q":
        break
    
    # 2. Handle View Change Commands (V/v and D/d)
    elif operation == "v":
        current_view = VIEW_CALCULATION
        print("View changed to CALCULATION mode (shows formula).")
        continue 
    elif operation == "d":
        current_view = VIEW_DEFAULT
        print("View changed to DEFAULT mode (shows result only).")
        continue

    try:
        # Dictionary to map operation number to a descriptive shape name
        shape_names = {
            "1": "rectangle", "2": "circle", "3": "triangle",
            "4": "sphere", "5": "cube"
        }
        
        # Initialize result and calculation string variables
        result = None
        calc_str = ""

        # --- Handle Calculation Operations ---
        if operation == "1":
            a = get_positive_value("What is side A? ")
            b = get_positive_value("What is side B? ")
            result, calc_str = area_rectangle(a, b) 
            
        elif operation == "2":
            r = get_positive_value("What is the radius? ")
            result, calc_str = area_circle(r)

        elif operation == "3":
            b = get_positive_value("What is the base? ")
            h = get_positive_value("What is the height? ")
            result, calc_str = area_triangle(b, h)

        elif operation == "4":
            r = get_positive_value("What is the radius? ")
            result, calc_str = volume_sphere(r)

        elif operation == "5":
            s = get_positive_value("What is the side length? ")
            result, calc_str = volume_cube(s)
        
        else:
            print("Invalid selection. Please enter a number (1-5), 'q' to quit, 'v' for calculation view, or 'd' for default view.")
            continue # Skip printing separator if input was invalid

        
        #  different outputs based on View Mode 
        
        # Get the operation type (Area or Volume) and shape name
        if operation in ["1", "2", "3"]:
            op_type = "area"
        else: # operation in ["4", "5"]
            op_type = "volume"
            
        shape_name = shape_names.get(operation)

        # Print the calculation, optional
        if current_view == VIEW_CALCULATION:
            print(f"Calculation: {calc_str}")

        # Print the final result
        print(f"The {op_type} of this {shape_name} is: {result:.2f}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please ensure your inputs are valid numbers.")

    print("-------------------------------") #arbitrary layout tinkering
 
 
# tack on a mainguard feature...
if __name__ == '__main__':
    main()
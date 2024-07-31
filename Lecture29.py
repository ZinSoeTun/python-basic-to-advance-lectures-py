# if __name__ == __main__: (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing

# Good practice (code is modular, helps readability, leaves no global variables, avoids unintended execution)

# Ex. library = Import library for functionality.
#                       When running library directly, display a help page

# ---------- script1.py ----------
# This file can run standalone or be imported

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()

# ---------- script2.py ----------
# This file should run only standalone

from Lecture24 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

print("This is Lecture24")
favorite_food("sushi")
favorite_drink("coffee")
print('Goodbye!')
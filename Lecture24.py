# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate file

import Lecture25

# result = Lecture25.pi
# result = Lecture25.square(3)
# result = Lecture25.cube(3)
# result = Lecture25.circumference(3)
result = Lecture25.area(3)

print(result)
# print(help())

def favorite_food(food):
    print(f"Your favorite food is {food}")
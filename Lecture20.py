# Positional and Default Arguments

# default arguments = A default value for centain parameters
#                     default is used when that argument is omitted
#                     make your function more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# ----- EXAMPLE -----
def net_price(list_price, discount=0, tax=0.05):
   return list_price * (1 - discount) * (1 - tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# ----- EXERCISE -----
import time

def count(end, start=0): 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(10)
# count(30, 15)
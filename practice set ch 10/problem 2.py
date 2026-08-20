n = int(input("enter your number: "))
square = n*n
cube = n*n*n
import math
squareroot = math.sqrt(n)

class calculator:
    def __init__(self,square,cube,squareroot):
        self.square = square
        self.cube = cube
        self.squareroot = squareroot

c = calculator(square,cube,squareroot)

print(c.square,c.cube,c.squareroot)


# type 2

import math
class calculator:
    def __init__(self,n):
        self.square = n*n
        self.cube = n*n*n
        self.squareroot = math.sqrt(n)

n = int(input("enter your number: "))
c = calculator(n)
print(c.square, c.cube, c.squareroot)
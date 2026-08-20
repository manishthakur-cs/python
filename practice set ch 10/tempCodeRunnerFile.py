import math
class calculator:
    def __init__(self,n):
        self.square = n*n
        self.cube = n*n*n
        self.squareroot = math.sqrt(n)

n = int(input("enter your number: "))
c = calculator(n)
print(c.square, c.cube, c.squareroot)
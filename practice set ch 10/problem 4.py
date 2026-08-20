import math
class calculator:
    def __init__(self,n):
        self.square = n*n
        self.cube = n*n*n
        self.squareroot = math.sqrt(n)
    @staticmethod
    def hello():
        print("your calculattor is ready")



n = int(input("enter your number: "))
c = calculator(n)
calculator.hello()

print(c.square, c.cube, c.squareroot)
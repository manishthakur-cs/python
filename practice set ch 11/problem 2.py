class animals:
    pass

class pets(animals):
    pass

class dog:
    @staticmethod
    def bark():
        print("bow bow!")

d = dog()
d.bark()

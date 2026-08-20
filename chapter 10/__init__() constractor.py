class employee :
    
    salary = 2400000
    company = "data handler" #this is a class attributes

    def __init__(self, name, salary, company):         # dunder method which is automatically call karta hai jab bhi nya object bnta hai
        self.name = name
        self.salary = salary
        self.company = company

        print("i am creating an object")

    def getinfo(self):
        print(f"the company is {self.company},the salary is {self.salary}")

    def greet(self):
        print ("hello world")

manish = employee("manish", 240000,"data handler")


manish.name = "manish" #this is an instance attributes 
print(manish.name , manish.salary , manish.company)  # line no 13 or 11 dono same hai likhne ka trika alg  alg hai

manish.getinfo()
manish.greet()
print(manish.name,manish.salary)
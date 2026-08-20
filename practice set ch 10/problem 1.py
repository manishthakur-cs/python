name = input("enter your name: ")
salary = int(input("enter your salary: "))
pincode = int(input("enter your pincode: "))

class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = programmer(name,200000,527543)
print(p.name,p.salary,p.pincode,p.company)
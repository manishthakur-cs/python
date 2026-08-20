# static method ko  object ki jrurat nahi hai, or ye ek docarator hota hai.(line no 14 me lga hai jo wahi hai static method)


class employee :

    
    salary = 2400000
    company = "data handler" #this is a class attributes

    def getinfo(self):
        print(f"the company is {self.company},the salary is {self.salary}")


    @staticmethod
    def greet(self):
        print ("hello world")

manish = employee()
manish.name = "manish" #this is an instance attributes 
print(manish.name , manish.salary , manish.company)  # line no 13 or 11 dono same hai likhne ka trika alg  alg hai

manish.getinfo()
manish.greet()
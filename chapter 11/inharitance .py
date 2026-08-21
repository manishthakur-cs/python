class employee:
    company = " itc "
    name = "default name"
    def show(self):
        print(f"the name is {self.name}and the company is {self.company}")

class coder :
    language = "python"
    def printlanguage(self):
        print(f"out of all the language here is your language :{self.language}")




# method 1
# class programmer:
#     company = "itc infotech"
#     def show(self):
#         print(f" the name is {self.name}and the salary is {self.slary}")
    
#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with{self.language} language")
#method 2
class programmer(employee,coder):
    company = "itc tech"
    def showlanguage(self): 
        print(f"the name is {self.company} and he is good with {self.language} language")



a = employee()
b = programmer()

b. show ()
b.printlanguage()
b.showlanguage()
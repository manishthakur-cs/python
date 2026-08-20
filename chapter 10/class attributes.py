class employee :
    
    salary = 2400000
    company = "data handler" #this is a class attributes

manish = employee()
manish.name = "manish" #this is an instance attributes 
print(manish.name , manish.salary , manish.company)

avinash = employee()
avinash.name = "avinash"
print(manish.salary, manish.company, manish.name)

# here name is instance attributes and salary and language are class attributes as they directly belong to the class

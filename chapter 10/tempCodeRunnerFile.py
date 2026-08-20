class employee :
    
    salary = 2400000
    company = "data handler" #this is a class attributes

manish = employee()
manish.name = "manish" #this is an instance attributes 
print(manish.name , manish.salary , manish.company)

avinash = employee()
avinash.company = "google"
print(manish.salary, manish.company, avinash.company)  # dekho ek baat humesha dhyan me rkho ki class attributes se pehle instance attributes ayega samjha.


# here name is instance attributes and salary and language are class attributes as they directly belong to the class

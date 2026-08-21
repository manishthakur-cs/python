class employee:
    a = 1 

    @classmethod
    def show (cls):
        print(f"the class attributes of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.mname} {self.lname}"

    @name.setter
    def name (self , value):
        self.fname = value.split(" ")[0]
        self.mname = value.split(" ")[1]
        self.lname = value.split(" ")[2]
        
   

e = employee()
e.a = 45

e.name = "manish kumar thakur"
print(e.name)

e.show()
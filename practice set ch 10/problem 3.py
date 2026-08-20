class demo:
    a = 4 

o = demo()
print(o.a) # print the class attribute because instance
o.a = 0 #instance attribute is set
print(o.a) # print the instace attributes because instance attributes is present 

print(demo.a)
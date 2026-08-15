f = open("file.txt")
print(f.read())
f.close()


# the same can be written using with statemnt like this

with open ("file.txt" , "r") as f:
    print(f.read())
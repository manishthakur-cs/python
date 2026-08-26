n = int(input("enter your number : "))

table = [n*i for i in range(1,11)]

with open ("table.txt","a") as f:
    f.write (f"table of {n} : {str(table)}  \n") # is line ko dusre trike se bhi likh skta huu.and

     #f.write(str(table) + "\n")


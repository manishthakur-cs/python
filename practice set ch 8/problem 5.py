'''
n = 3
1 2 3
1 2
1

n = (n)
n = (n-1)
n = (n-2)
'''
n = int(input("enter your number : "))

def pattern(n):
    if (n == 0):
        return 
    print("*" * n)
    pattern(n-1)

pattern(n)
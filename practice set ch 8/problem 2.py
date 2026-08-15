''' 
celsius to fahrenheit
celsius = ( celcius * 9/5) + 32
'''
def f_to_c(f):
    return (f * 9/5) +32

f = int (input("enter temperature in f : "))
c = f_to_c(f)
print( f" {round(c,2)}  degree celsius ")
#This program will show you all of the common integers between two randomly generated lists.
import random
a = []
b = []
c = []

def generate_list(variable):
    for n in range(0,15):
        variable.append(random.randint(1,20))
    return variable

def check_duplicates():
    for n in a:
        if n in b:
            c.append(n)
    print(c)

    
generate_list(a)
generate_list(b)
print(a)
print(b)
check_duplicates()
number = int(input("Enter a number, and I will tell you all of that numbers' divisors: "))
divisor_list = []
for n in range(1, number+1):
    if(number % n == 0):
        divisor_list.append(n)
print(divisor_list)
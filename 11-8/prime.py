message = ""
number = int(input("Enter a number and we will determine if it is a prime number or not: "))
for count in range(2,number):
    if(number % count == 0):
        message = "Not Prime!"
        break
    else:
        message = "Prime!"
print(message)


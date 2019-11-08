number = int(input("Enter a number to find the factorial of said number: "))
factorial = 1
for number in range(1, number + 1):
    factorial = number * factorial
print(factorial)
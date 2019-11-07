#Program will print "fizz" if input is divisible by 3, and "buzz" if divisible by 5. if divisible by both, result is "fizzbuzz"

user_choice = int(input("Enter any number to determine whether that number will Fizz, Buzz, or both: "))

if(user_choice % 5 == 0) and (user_choice % 3 == 0):
    print("fizzbuzz")
elif(user_choice % 3 == 0):
    print("fizz")
elif(user_choice % 5 == 0):
    print("buzz")
else:
    print("This number will neither fizz, nor buzz. Sorry!")
    
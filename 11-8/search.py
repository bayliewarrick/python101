search = [1,2,3,4,5,6,7,8,10]
user_input = int(input("Enter a number and we will return whether or not the number is found in the array: "))

if user_input not in search:
    print("Number not found!")
else:
    print("Found!")
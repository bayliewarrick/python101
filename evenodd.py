#This program will determine if an inputted number is even or odd.
user_choice = int(input("Enter any number to determine whether that number is even or odd: "))

if(user_choice % 2 == 0):
    print(f"{user_choice} is an EVEN number.")
elif(user_choice % 2 != 0):
    print(f"{user_choice} is an ODD number.")
else:
    print("Error!")
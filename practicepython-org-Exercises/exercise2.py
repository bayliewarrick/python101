#Tells user whether the number given is odd or even.
given = int(input("Enter any number, we will tell you if the number is odd or even: "))

if given % 2 == 0:
    odd_or_even = "EVEN"
elif given % 2 != 0:
    odd_or_even = "ODD"

print("****************************")
print(f"*     {given} is an {odd_or_even} number!  *")
print("****************************")
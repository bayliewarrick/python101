
result = 0

def ask_user_for_input(): 
  number1 = int(input("Enter number 1: "))
  operand = input("Enter Operand (+,-,*,/): ")
  number2 = int(input("Enter number 2: ")) 
  return (number1, operand, number2)

def add(a,b):
  return a+b 

def subtract(a,b):
  return a-b 

def display_result(a,b,op,result): 
  print("***********************************")
  print(f"{a} {op} {b} = {result}")
  print("***********************************")


(no1,op,no2) = ask_user_for_input()

if no1 % 2 == 0: 
  print("EVEN")
else: 
  print("ODD")


if op == "+": 
  result = no1 + no2 

if op == "-": 
  result = no1 - no2 

if op == "*": 
  result = no1 * no2 




if op == "+":
  result = add(no1,no2)
elif op == "-":
  result = subtract(no1,no2)
elif op == "*": 
  result = no1 * no2 
else: 
  print("unknown operand!")

display_result(no1,no2,op,result)




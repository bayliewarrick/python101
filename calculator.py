#calculates the result of two numbers and an operand.
def takeinputs():
    input1 = int(input("Enter the first number for your calculation: "))
    input2 = input("Enter the operation desired (+, -, *, /):")
    input3 = int(input("Enter the second number for your calculation: "))
    return input1, input2, input3

def calc():
    (input1,input2,input3) = takeinputs()
    if input2 == "+":
        result = input1 + input3
    elif input2 == "-":
        result = input1 - input3
    elif input2 == "*":
        result = input1 * input3
    elif input2 == "/":
        result = input1 / input3
    else: 
        input2 = input("Enter the operation desired (+, -, *, /):")
        input3 = int(input("Enter the second number for your calculation: "))
    print(f"{input1} {input2} {input3} equals {result}")


calc()




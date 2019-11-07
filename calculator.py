#calculates the result of two numbers and an operand.
def takeinputs():
    input1 = int(input("Enter the first number for your calculation: "))
    input2 = input("Enter the operation desired (+, -, *, /):")
    input3 = int(input("Enter the second number for your calculation: "))
    return input1, input2, input3

def add(input1, input3):
    total = input1 + input3
    return total    

def sub(input1, input3):
    total = input1 - input3
    return total

def mul(input1, input3):
    total = input1 * input3
    return total  

def div(input1, input3):
    total = input1 / input3
    return total    


def calc():
    (input1,input2,input3) = takeinputs()

    if input2 == "+":
        result = add(input1, input3)
    elif input2 == "-":
        result = sub(input1, input3)
    elif input2 == "*":
        result = mul(input1, input3)
    elif input2 == "/":
        result = div(input1, input3)
    else: 
        input2 = input("Enter the operation desired (+, -, *, /):")
        input3 = int(input("Enter the second number for your calculation: "))
    print(f"{input1} {input2} {input3} equals {result}")


calc()
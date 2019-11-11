#calculates the result of two numbers and an operand.
input1 = 0
input3 = 0

def takeinputs():
    input1 = int(input("Enter the first number for your calculation: "))
    input2 = input("Enter the operation desired (+, -, *, /):")
    input3 = int(input("Enter the second number for your calculation: "))
    return input1, input2, input3

def add(input1, input3):
    return (input1 + input3)
        
def sub(input1, input3):
    return (input1 - input3)

def mul(input1, input3):
    return (input1 * input3) 

def div(input1, input3):
    return (input1 / input3)    

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
        print("Invalid Operand! Please try again.")
        calc()
    print(f"{input1} {input2} {input3} equals {result}")
    again = input('Press "A" to calculate another equation. press any other key to exit program.').upper()
    if(again == 'A'):
        calc()
    else:
        print("Exiting Program!")
        exit(1000)
    
    




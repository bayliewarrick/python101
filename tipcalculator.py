def tipcalculator():
    total = int(input("Enter the total, before tip: "))
    tip = int(input("Enter the percentage that you would like to tip, in whole numbers: ")) / 100
    total += (total * tip)
    print(total)
tipcalculator()
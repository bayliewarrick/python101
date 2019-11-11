"""
car = {
    'Make': 'Honda',
    'Model': 'Accord',
    'Year': '1990',
    'cyl': '4'
}
"""
car = {}
cars = []


while True:
    make = input("Enter make: ")
    model = input("Enter model: ")

    car = {"make": make, "model": model}
    cars.append(car)

    print(cars)
    
    choice = input("Enter q to quit or any other key to continue")
    if(choice == "q"):
        break
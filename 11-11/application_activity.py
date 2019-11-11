persons = []


while True:
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    age = int(input("Enter age: "))

    person = {
        'firstname': first,
        'lastname': last,
        'age': age
    }

    persons.append(person)

    choice = input("Enter q to quit or any other key to continue")
    if(choice == "q"):
        break
    
print(persons)
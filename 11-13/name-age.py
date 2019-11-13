""""
input name and age,
create dictionary with name and age
add to users.append()
wrote array to json
"""
import json
users = []
while True:
    name = input("Enter your name:")
    age = input("Enter your age: ")
    user = {'name': name, 'age': age}
    users.append(user)
    with open('users.json','w') as file_object:
        f = json.dump(users,file_object)
    print(users)

 
    
    
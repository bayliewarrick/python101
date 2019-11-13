"""
#open file in write mode
file_object = open('todo.txt','w')
file_object.write('hello, python!')
file_object.close()


#better way to write to file, will automatically close for you.
with open('todo.txt', 'w') as file_object:
    file_object.write("Hello world!!!")

#read text from file:

with open('MyTasks.txt') as file_object:
    contents = file_object.read()
    print(contents) # or print(contents.rstrip())


#json
{
    'name':john #valid json
}

#json 2
  invalid json:
{
    'name': 'john' 
}

{
    'name':'mary'
}
"""




import json

class Customer:
    def __init__(self,name):
        self.name = name
    def to_dictionary(self):
        return self.__dict__
    def create_customer_from_dict(dictionary):
        return Customer(dictionary['name'])    

customer = Customer("john doe")
"""
with open('customers.json','w') as file_object:
    json.dump(customer.to_dictionary(), file_object)
"""

#reading back an object from json
with open('customers.json') as file_object:
    customer_dictionary = json.load(file_object)
    print(customer_dictionary)
    customer = create_customer_from_dict(customer_dictionary)
    print(customer)
    print(customer.name)
    


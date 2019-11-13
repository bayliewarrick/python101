name = input("Enter your name here. it will save to MyName.txt ")
with open('MyName.txt','w') as file_object:
    file_object.write(name)
    file_object.write('\r')

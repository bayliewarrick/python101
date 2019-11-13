import json #imports json module

tasks = []
task = {'name': 'wash the car', 'priority': 'medium'}

tasks.append(task)

#to write a json file:

with open('tasks.json','w') as file_object:
    json.dump(task,file_object)

#to read a json file:
with open('tasks.json') as file_object:
    some_task = json.load(file_object)
    print(some_task)

task2 = {"name":'blah', 'priotity':'high'}
tasks.append(task2)

with open('tasks.json','w') as file_object:
    json.dump(tasks, file_object)
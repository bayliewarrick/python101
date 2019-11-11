tasks = []
menuoptions = ['1','2','3','4', 'q']

def user_choice():
    while True:
        choice = input("MENU: 1 to ADD TASK, 2 to DEL TASK, 3 to VIEW ALL TASKS, q to QUIT")
        if choice in menuoptions:
            if(choice == '1'):
                add_task()
            elif(choice == '2'):
                del_task()
            elif(choice == '3'):
                show_tasks()
            elif(choice == 'q'):
                break

def add_task():
    title = input("Enter a task here: ")
    priority = input("is this task High, Medium, or Low priority?: ")
    task = {
    'title': title,
    'priority': priority
    }

def del_task():
    show_tasks()
    to_delete = int(input("Enter the index value of the task you wish to delete: "))
    del tasks[to_delete]

def show_tasks():
    for task in tasks:
        print(f"{tasks.index(task)} - {task['title']} - {task['priority']}")
    print(sorted)

user_choice()



import json

#Variables
to_do_list = []
completed_tasks = []
intro_msg = ('Welcome to Task Manager How can I help you today')

#add task function
def add_task():
    task = input('What task would you like to add: ').split()
    to_do_list.append(task)
    return

while True: 
    print(intro_msg)
    ask = input('1. See list ' '2. Add task ' '3. Delete Task ' '4. Add to completed')
    if ask == '1' or 'See list':
        print(to_do_list)
    break


    





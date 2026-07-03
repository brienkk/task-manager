import json

#Variables
to_do_list = []
completed_tasks = []
intro_msg = ('Welcome to Task Manager How can I help you today')

#add task function
def add_task():
    task = input('What task would you like to add: ').split(',')
    to_do_list.extend(task)

#show list function
def show_list():
    for number, list_item in enumerate(to_do_list, start=1):
        print(f"{number}, {list_item}")
#function for deleting items from lists    
def delete_task():
    print(show_list())
    task_to_delete = input('What item would you like to remove from the list, use a number')
    task_number = int(task_to_delete)
    task_string = to_do_list.pop(task_number - 1)
    
#function for adding items to completed list 
def task_finished():
    print(show_list())
    task_to_move = input('What task have you finished')
    task_number = int(task_to_move)
    task_string = to_do_list.pop(task_number - 1)
    completed_tasks.append(task_string)

while True: 
    print(intro_msg)
    ask = input('1. See list ' '2. Add task ' '3. Delete Task ' '4. Add to completed ' '5. Quit' )
    if ask == '1' or ask == 'See list':
        print(show_list())
    elif ask == '2' or ask == 'Add task':
        add_task()
    elif ask == '3' or ask == 'Delete task':
        delete_task()
    elif ask == '4' or ask == 'Add to completed':
        task_finished()
        print(completed_tasks)
    elif ask == '5' or ask == 'quit':
        break
    else:
        print('That is not a valid answer please choose either the number or the name of what you want to do' )
    




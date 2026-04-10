#maintain list
#add task
#remove task
#view tasks

tasks =[]

def view_tasks():
    print("\n Your To-Do List:")
    for index,task in enumerate(tasks):
        print(f"{index} : {task["name"]} - {task["status"]}")
def add_task():
            new_task = input("Enter the task you want to add: ")
            task = {"name": new_task, "status": False}
            tasks.append(task)
            print(f"'{new_task}' added successfully!")

while True:        
        
        
    print("\n ==== To-Do List Menu ====")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_tasks()

    elif choice == 2: 
        add_task()
    elif choice == 3:
        task_index = int(input("Enter the index of the task you want to remove: "))
        tasks.pop(task_index)
        print("Task removed successfully!")
    elif choice == 4:
        task_index = int(input("Enter the index of the task you want to mark as completed: "))
        tasks[task_index]["status"] = True
        print("Task marked as completed!")
    elif choice == 0:
        print("Exiting the To-Do List. Goodbye!")
        break
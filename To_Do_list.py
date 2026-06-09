import sys
import json
To_do_List = []

# Function to Add Task
def add_task():
    task = input("Enter a task:")
    if task.strip() == "":
        print("Task cannot be empty!")
        return
    priority = input("Enter priority(high/medium/low):").strip().lower()
    if priority not in ["high","medium","low"]:
        print("Invalid Priority!")
        return
    due_date = input("Enter Dur date(DD-MM-YYYY):")
    To_do_List.append({"Task": task, "Status": "Pending" , "Priority": priority , "Due Date": due_date })
    save_tasks()
    print("Task added sucessfully! \n")

# Function to View Task 
def view_tasks():
    print("Your To-do List:")
    if len(To_do_List) == 0 :
        print("No Pending tasks!")
    else:
        print(f"Total Task: {len(To_do_List)}")
        for index , task in enumerate(To_do_List , start = 1):
            print(f"{index}.{task['Task']}\n Status: {task['Status']}\n Priority: {task['Priority'].capitalize()}\n Due Date: {task['Due Date']}")
    print('\n')

# Function to Delete Task
def delete_task():
    if(len(To_do_List ) == 0):
        print("No tasks avilable to delete!\n")
    else:
        try:
            view_tasks()
            search_index = int(input("Enter the task number that you want to remove :")) -1
            if 0 <= search_index < len(To_do_List):
                removed_task = To_do_List.pop(search_index)
                save_tasks()
                print(f"Task Removed : {removed_task['Task']}")
            else:
                print("Invalid Task")
        except ValueError:
            print("Please Enter a valid Task Number.")

# Function to Mark completed Task
def mark_as_completed():
    if len(To_do_List) == 0:
        print("No tasks available.")
    else:
        try:
            view_tasks()
            search_index = int(input("Enter the task number that you want to mark as complete: ")) -1
            if 0 <= search_index < len(To_do_List):
                To_do_List[search_index]['Status'] = 'Done'
                save_tasks()
                print(f"Task {To_do_List[search_index] ['Task']} has been marked as Done.")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please Enter a valid Task NUmber.")


# Function to Exit
def exit_program():
    confirmation = input("Are you sure want to Exit?")
    if confirmation.lower() in ["yes" , "y"]:
        print("You Exit sucessfully!")
        sys.exit()
    else :
        print("Exit cancelled.")

# Function to save
def save_tasks():
    with open("task.json","w") as file:
        json.dump(To_do_List,file , indent = 4)

# function for loading Task
def load_task():
    global To_do_List
    try:
        with open("task.json","r") as file:
            To_do_List = json.load(file)
    except FileNotFoundError:
        To_do_List

        
        
# Features 
def features():
    while(True):
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Mark a Task as completed")
        print("5. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_as_completed()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid Choice! Please try again.")
load_task()
features()




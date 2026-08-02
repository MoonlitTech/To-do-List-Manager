# Imports JSON library to allow user to save and load task data
import json

# Stores all created tasks 
tasks = []

'''
This function controls the main program flow.
main() loads all saved tasks, displays the menu, receives user choices, and calls the desired function based on the user's selection.
'''
def main():
    # Loads previously saved tasks when the program starts
    load_tasks()

    # Displays the program introduction and explains the purpose of the application 
    print("--------------------\n    Task Manager\n--------------------")
    print("Welcome to the To-do List Manager!\nThis is a personal task manager to help organize your tasks and keep track of your progress!")

    # Stores the user's menu selection and keeps the program running until the user chooses to exit the program  
    choice = ""

    ## While loop to keep repeating menu 
    while choice != "5":
        print("--------------------")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Task")
        print("4. Complete Task")
        print("5. Exit")
        print("--------------------")

        choice = input("Enter your choice: ")

        # Calls the function associated with the user's menu choice
        if choice == "1": 
            add_task()
        elif choice == "2": 
            delete_task()
        elif choice == "3": 
            view_task()
        elif choice == "4": 
            complete_task()
        elif choice == "5": 
            save_tasks()
            print("Thank you for using the Task Manager, see you next time!")
        else: 
            print("Please only enter numbers.")

''' 
Adds new tasks to the task list. 
Uses dictionaries to store each task's name and completion status.
Allows users to add multiple tasks until they choose to stop.
'''
def add_task():
    cont_adding = True
    while cont_adding == True:
        # Gets the task name from the user and creates a task dictionary 
        task_name = input("Enter your task: ")
        given_task = {
            "name": task_name, 
            "status": False
            }

        # Adds the new task dictionary to the task list 
        tasks.append(given_task)
        print("Tasked added!")

        # Allows the user to continue adding tasks without returning to the menu until they decide to stop 
        user_cont = input("Do you wish to add another task? (y/n): ")
        if user_cont == "y":
            cont_adding = True 
        else:
            cont_adding = False

''' 
Deletes a selected task from the task list.
Displays available tasks, receives the user's selection, and removes the chosen task using its list index.
'''
def delete_task():
    if len(tasks) != 0: 
        view_task()
        user_del = int(input("Enter a task to delete: "))

        # Checks that the selected task number exists before deleting by converting users choice into correct index values 
        if user_del >= 1 and user_del <= len(tasks): 
            # Converts user input into the correct list index
            tasks.pop(user_del - 1)
            print("Task is now deleted!")
        else:
            print("Invalid input.")
        view_task()
    else: 
        print("No tasks available.")

'''
Displays all current tasks.
Uses loops, dictionaries, and conditional statements to show each task's name and completion status.
'''
def view_task():
    if len(tasks) == 0:
        print("There are no tasks!")
    else: 
        print("Current Tasks: ")
        count = 1

        # Loops through each dictionary in the task list
        for given_task in tasks: 
            # Determines whether the task is complete or incomplete 
            if given_task["status"]:
                status = "Complete"
            else:  
                status = "Incomplete"

            print(f"{count}. {given_task["name"]} - {status}")
            count += 1 

'''
Marks a selected task as complete.
Allows the user to choose a task and updates the dictionary value from incomplete (False) to complete (True).
'''
def complete_task():
    if len(tasks) != 0: 
        view_task()
        user_comp = int(input("Enter a task to complete: "))
        
        if user_comp >= 1 and user_comp <= len(tasks): 
            tasks[user_comp - 1]["status"] = True 
            print("Task is now completed!")
        else: 
            print("Invalid input.")
        view_task()
    else: 
        print("No tasks available.")

'''
Saves the current task list into a JSON file.
Converts the Python list of dictionaries into a format that can be stored and loaded when the program runs again.
'''
def save_tasks():
    with open("tasks.json", "w") as file: 
        json.dump(tasks, file)

        print("Your tasks are now saved!")

'''
Loads previously saved tasks from the JSON file.
Restores the task list when the program starts.
Creates an empty list if no saved file exists.
'''
def load_tasks():
    global tasks 

    try: 
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    # Handles the first time the program runs when no file exists 
    except FileNotFoundError:
        tasks = []

# Starts the Task Manager program            
main()

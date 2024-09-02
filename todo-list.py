def get_user_choice():
    choice = input("Enter your choice: ")
    return(choice)

tasks = []
def add_task():
      new_task = input("Enter the task you want to add:")
      tasks.append(new_task)
      print("Task added successfully!")

def view_task():
    if not tasks:
        print("No tasks")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def mark_task_complete():
    view_task()
    task_number = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task completed")
    else:
        print("Invalid task number")

def delete_task():
     view_task()
     task_number = int(input("Enter the task number to delete: "))
     if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully!")
     else:
        print("Invalid task number")

def show_menu():
        print("1. add task")
        print("2. View Tasks")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")

def main():
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == "1":
                add_task()
        elif choice == "2":
                view_task()
        elif choice == "3":
                mark_task_complete()
        elif choice == "4":
                delete_task()
        elif choice == "5":
                print("Exiting...")
                break
        else:
            print("Invalid choice. Select again.")

if __name__ == "__main__":
    main()
# end main
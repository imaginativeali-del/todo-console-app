# Todo Console Application
# Phase 1 - Spec Driven (AI Assisted)

tasks = []
task_id_counter = 1


def add_task():
    global task_id_counter
    title = input("Enter task title: ")
    task = {
        "id": task_id_counter,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    task_id_counter += 1
    print("✅ Task added successfully!")


def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\nYour Tasks:")
    for task in tasks:
        status = "✔ Completed" if task["completed"] else "⏳ Pending"
        print(f'ID: {task["id"]} | {task["title"]} | {status}')


def complete_task():
    task_id = int(input("Enter task ID to mark complete: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("✅ Task marked as completed!")
            return
    print("❌ Task not found.")


def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("🗑 Task deleted!")
            return
    print("❌ Task not found.")


def show_menu():
    print("\n====== TODO APP ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()

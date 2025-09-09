import argparse, json, sys
from addTask import add_task
from listTasks import list_tasks
from checkTask import complete_check_task
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()  # Create an argument parser
    sub = parser.add_subparsers(dest="cmd")  # Create subparsers for commands

    # Add a task command
    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument(
        "task", type=str, help="Task Description"
    )  # Positional argument for task description

    # List tasks command
    sub.add_parser("list", help="List all stored tasks")  # Subparser for listing tasks
    # list_p.add_argument('completed', action="store_true", help="List all completed tasks")

    # Complete a task command
    check_p = sub.add_parser("check", help="Mark a task as completed")
    check_p.add_argument(
        "--all", action="store_true", help="Mark all tasks as completed"
    )
    check_p.add_argument(
        "--task_idx", type=int, help="Index of the task to mark as completed"
    )

    uncheck_p = sub.add_parser("uncheck", help="Mark a task as not completed")
    uncheck_p.add_argument(
        "--all", action="store_true", help="Mark all tasks as incomplete"
    )
    uncheck_p.add_argument(
        "--task_idx", type=int, help="Index of the task to mark as not completed"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Handle commands
    # If the command is 'add'
    if args.cmd == "add":
        try:
            task = args.task
            add_task(task)
        except Exception as e:
            print(f"Error adding task: {e}", file=sys.stderr)
            sys.exit(1)  # Exit with a non-zero status code on error
    # If the command is 'list'
    elif args.cmd == "list":
        try:
            list_tasks()
        except Exception as e:
            print(f"Error reading tasks: {e}", file=sys.stderr)
            sys.exit(1)
    # If the command is 'check'
    elif args.cmd == "check":
        try:
            if args.all:
                with open("tasks.json", "r+") as file:
                    try:
                        data = json.load(file)
                        if data:
                            for task in data:
                                task["completed"] = True
                            print("All tasks are marked as completed.")
                        else:
                            print("No tasks found.")
                            sys.exit(1)
                        # Move the file pointer to the beginning of the file
                        file.seek(0)
                        # Write the updated tasks back to the file
                        json.dump(data, file, indent=4)
                        # Remove any remaining data in the file after the current position
                        file.truncate()
                    except json.JSONDecodeError:
                        print("No tasks found.")
                        sys.exit(1)
                return
            else:
                task_idx = args.task_idx - 1
                with open("tasks.json", "r+") as file:
                    try:
                        data = json.load(file)
                        if data:
                            for idx, task in enumerate(data):
                                if idx == task_idx:
                                    task["completed"] = True
                                    print(f"Task '{task['task']}' marked as completed.")
                                    break
                        else:
                            print("No tasks found.")
                            sys.exit(1)
                        # Move the file pointer to the beginning of the file
                        file.seek(0)
                        # Write the updated tasks back to the file
                        json.dump(data, file, indent=4)
                        # Remove any remaining data in the file after the current position
                        file.truncate()
                    except json.JSONDecodeError:
                        print("No tasks found.")
                        sys.exit(1)
        except Exception as e:
            print(f"Error marking task as completed : {e}", file=sys.stderr)
            sys.exit(1)
    # If the command is 'uncheck'
    elif args.cmd == "uncheck":
        try:
            if args.all:
                print("Marking all tasks as not completed.")
                with open("tasks.json", "r+") as file:
                    try:
                        data = json.load(file)
                        if data:
                            for task in data:
                                task["completed"] = False
                        else:
                            print("No tasks found.")
                            sys.exit(1)
                        # Move the file pointer to the beginning of the file
                        file.seek(0)
                        # Write the updated tasks back to the file
                        json.dump(data, file, indent=4)
                        # Remove any remaining data in the file after the current position
                        file.truncate()
                    except json.JSONDecodeError:
                        print("No tasks found.")
                        sys.exit(1)
                return
            task_idx = args.task_idx - 1
            with open("tasks.json", "r+") as file:
                try:
                    data = json.load(file)
                    if data:
                        for idx, task in enumerate(data):
                            if idx == task_idx:
                                task["completed"] = False
                                print(
                                    f"Task '{task['task']}' is removed from completed."
                                )
                                break
                    else:
                        print("No tasks found.")
                        sys.exit(1)
                    # Move the file pointer to the beginning of the file
                    file.seek(0)
                    # Write the updated tasks back to the file
                    json.dump(data, file, indent=4)
                    # Remove any remaining data in the file after the current position
                    file.truncate()
                except json.JSONDecodeError:
                    print("No tasks found.")
                    sys.exit(1)
        except Exception as e:
            print(f"Error marking task as completed : {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # If no valid command is provided, display the help message
        parser.print_help()

if __name__ == "__main__":
    main()

import json,sys

def list_tasks() -> None:
    with open("tasks.json", "r") as file:
        try:
            data = json.load(file)
            if data:
                for idx, task in enumerate(data, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{idx}. [{status}] {task['task']}")
            else:
                print("No tasks found.")
        except json.JSONDecodeError:
            print("No tasks found.")
            sys.exit(0)
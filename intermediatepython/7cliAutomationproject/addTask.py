import json
from pathlib import Path

def add_task(task) -> None:
    json_dir = Path("tasks.json")
    # Ensure the directory exists
    if not json_dir.exists():
        json_dir.touch()  # Create the file if it doesn't exist
    with open("tasks.json", "r+") as file:
        try:
            data = json.load(file)  # Load existing tasks in the json file
        except (
                json.JSONDecodeError
        ):  # If file is empty or invalid, initialize data as an empty list
            data = []  # Initialize data as an empty list
        data.append({"task": task, "completed": False})
        file.seek(0)  # Move the file pointer to the beginning of the file
        json.dump(data, file, indent=4)
        print(f"Task '{task}' added successfully.")
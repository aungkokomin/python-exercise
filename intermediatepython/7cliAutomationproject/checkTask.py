import json, sys

def complete_check_task(file):
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

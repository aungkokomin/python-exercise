# import greet
# greet.hello("Pythonista")

try:
    n = int(input("Number:"))
    print(10/n)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input! Enter a number.")

try:
    with open("non_existent_file.txt") as f:
        content = f.read()
        if content == "":
            raise ValueError("File is empty")
except FileNotFoundError:
    print(f"File Not Found")
except IOError: # Catch other I/O related errors
    print("An I/O error occurred.")


def create_file():
    name = input("Enter file name: ")
    open(name, 'w').close()
    print("File created successfully!")

def write_file():
    name = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(name, 'w') as f:
        f.write(data)
    print("Data written successfully!")

def read_file():
    name = input("Enter file name: ")
    try:
        with open(name, 'r') as f:
            print("\nFile Content:")
            print(f.read())
    except FileNotFoundError:
        print("File malyo nahi!")

def append_file():
    name = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(name, 'a') as f:
        f.write("\n" + data)
    print("Data appended successfully!")

def menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        ch = input("Enter your choice: ")
        if ch == "1": create_file()
        elif ch == "2": write_file()
        elif ch == "3": read_file()
        elif ch == "4": append_file()
        elif ch == "5": break
        else: print(" choice!")
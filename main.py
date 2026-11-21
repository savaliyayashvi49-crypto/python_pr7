# PR. 7 - Moduler & Packager
# Multi-Utility Toolkit

import importlib
from my_toolkit import datetime_tools, math_tools, random_tools, uuid_tools, file_tools, convert_tools

def explore_module():
    name = input("Enter module name to explore: math / random / datetime / uuid: ")
    try:
        mod = importlib.import_module(name)
        print(f"\nAvailable Attributes in {name} module:")
        # dir() - Dynamic Exploration
        attrs = [a for a in dir(mod) if not a.startswith('_')]
        print(attrs)
    except ModuleNotFoundError:
        print("Aavu module nathi!")

def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Unit Conversions (Custom Module)")
        print("7. Explore Module Attributes (dir())")
        print("8. Exit")
        print("==============================")
        ch = input("Enter your choice: ")

        if ch == "1": datetime_tools.menu()
        elif ch == "2": math_tools.menu()
        elif ch == "3": random_tools.menu()
        elif ch == "4": uuid_tools.generate_uuid()
        elif ch == "5": file_tools.menu()
        elif ch == "6": convert_tools.menu()
        elif ch == "7": explore_module()
        elif ch == "8":
            print("\n==============================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("==============================")
            break
        else:
            print("Khoto choice! Fari try karo.")

# __name__ and __main__ paradigm
if __name__ == "__main__":
    main()

import time
from datetime import datetime, date

def show_current_datetime():
    now = datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Day: {now.strftime('%A')}, Date: {now.strftime('%d %B %Y')}")

def date_difference():
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        date1 = date.fromisoformat(d1)
        date2 = date.fromisoformat(d2)
        diff = abs((date2 - date1).days)
        print(f"Difference: {diff} days")
    except ValueError:
        print("Sachi date format nakho! Ex: 2025-01-04")

def format_date():
    try:
        d = input("Enter date (YYYY-MM-DD): ")
        dt = datetime.fromisoformat(d)
        print("1. DD/MM/YYYY ->", dt.strftime("%d/%m/%Y"))
        print("2. Month Day, Year ->", dt.strftime("%B %d, %Y"))
        print("3. DD-Mon-YY ->", dt.strftime("%d-%b-%y"))
        print("4. Full ->", dt.strftime("%A, %d %B %Y %I:%M %p"))
    except ValueError:
        print("Sachi date nakho!")

def stopwatch():
    print("Stopwatch start thayu... Enter dabavo stop karva mate")
    input("Start karva Enter dabavo...")
    start = time.time()
    input("Stop karva Enter dabavo...")
    end = time.time()
    print(f"Elapsed Time: {end - start:.2f} seconds")

def countdown():
    try:
        sec = int(input("Enter seconds for countdown: "))
        for i in range(sec, 0, -1):
            print(i, end="... ", flush=True)
            time.sleep(1)
        print("\nTime's Up!")
    except ValueError:
        print("Number nakho!")

def menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        ch = input("Enter your choice: ")
        if ch == "1": show_current_datetime()
        elif ch == "2": date_difference()
        elif ch == "3": format_date()
        elif ch == "4": stopwatch()
        elif ch == "5": countdown()
        elif ch == "6": break
        else: print("Khoto choice!")
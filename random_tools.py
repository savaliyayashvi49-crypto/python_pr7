
import random
import string

def random_number():
    a = int(input("Enter start: "))
    b = int(input("Enter end: "))
    print(f"Random Number: {random.randint(a, b)}")

def random_list():
    n = int(input("Ketla numbers joiye? "))
    lst = [random.randint(1, 100) for _ in range(n)]
    print(f"Random List: {lst}")
    print(f"Random Choice from list: {random.choice(lst)}")
    print(f"Random Sample (3): {random.sample(lst, min(3, len(lst)))}")

def random_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")

def random_otp():
    otp = random.randint(100000, 999999)
    print(f"Generated OTP: {otp}")

def dice_game():
    print(f"Dice Rolled: {random.randint(1, 6)} 🎲")

def menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Dice Game")
        print("6. Back to Main Menu")
        ch = input("Enter your choice: ")
        if ch == "1": random_number()
        elif ch == "2": random_list()
        elif ch == "3": random_password()
        elif ch == "4": random_otp()
        elif ch == "5": dice_game()
        elif ch == "6": break
        else: print("choice!")
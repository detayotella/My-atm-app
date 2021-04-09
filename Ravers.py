# Ravers bank Atm app

import random
from datetime import datetime

ravers_database = {}

def init():
    "Initalize ravers database"
    valid_options = False
    print("Welcome to Ravers Bank")

    while valid_options == False:

        account_exist = int(input("Do you have an existing account: 1 (yes) 2 (no) \n"))

        if account_exist == 1:
            valid_options = True
            
            login()

        elif account_exist == 2:
            valid_options = True

            register()

        else: 
            print("You selected an invalid option")

def login():
    """Login into existing account"""
    print("Please login into your ravers account")
    personal_email = input("Please enter your email: ")
    personal_password = input("Please enter your password: ")

    for personal_email, personal_password in ravers_database.items():
        print("Login Successfull")

    ravers_operations()

def register():
    """Registration of an account"""

    print("******Register*******")
    email = input("Please enter your email address? \n")
    first_name = input("Please enter your first name? \n")
    last_name = input("Please enter your last name? \n")
    password = input("Please enter your personal password? \n")
    today = datetime.now()
    print(f"Account created at {today}")

    account_number = generating_account_number()
    ravers_database[account_number] = [ first_name, last_name, email, password]

    login()

def ravers_operations():
    """Service rendered by ravers bank"""
    print("Please select an option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Bills")
    print("4. Complaint")

    selected_options = int(input("please select an option"))

    if selected_options == 1:
        print(f"You selected option {selected_options}")
        withdrawal()
    elif selected_options == 2:
        print(f"You selected option {selected_options}")
        deposit()
    elif selected_options == 3:
        print(f"You selected option {selected_options}")
        bills()
    elif selected_options == 4:
        print(f"You selected option {selected_options}")
        complaint()
    else:
        print("You selected an invalid option")

def withdrawal():
    """Withdrawal of money from account"""
    print("Please select an option")  
    print("1. 1000")  
    print("2. 2000")
    print("3. 5000")
    print("4. 10000")
    print("5. other options")

    withdrawal_option = int(input("Please select an option"))

    if withdrawal_option == 1:
        print("Processing....")
        print("Take your cash")
        print("Thanks for using ravers bank")

    elif withdrawal_option == 2:
        print("Processing...")
        print("Take your cash")
        print("Thanks for using ravers bank")

    elif withdrawal_option == 3:
        print("Processing....")
        print("Take your cash")
        print("Thanks for using ravers bank")

    elif withdrawal_option == 4:
        print("Processing....")
        print("Take your cash")
        print("Thanks for using ravers bank")

    elif withdrawal_option == 5:
        print(input("Please enter your amount: "))
    
    else:
        print("Invalid options selected")

def deposit():
    """Deposit an amount in your account"""
    print(input("How much do you want to deposit: "))
    print("Processing....")
    print("Successfull")
    print("Thanks for using ravers bank")

def bills():
    """Payment of bills"""
    print("1. CableTv")
    print("2. Electricity")
    print("3. Water")
    print("4. Airtime")

    bills_options = int(input("Please selected an option: "))

    if bills_options == 1:
        print(f"You selected option {bills_options}")
        cabletv()
    elif bills_options == 2:
        print(f"You selected option {bills_options}")
        electricity()
    
    elif bills_options == 3:
        print(f"You selected option {bills_options}")
        print(input("Please enter an amount: "))
        print("Processing...")
        print("Thanks for using ravers bank")

    elif bills_options == 4:
        print(f"You selected option {bills_options}")
        airtime()

    else:
        print("Invalid option selected")

def cabletv():
    """Cable tv payment"""
    print("1. Gotv")
    print("2. Dstv")
    print("3. Startimes")

    cabletv_options = int(input("Please select an option: "))

    if cabletv_options == 1:
        print(input("Please enter an amount"))
        print("Processing...")
        print("Successfull")
        print("Thanks for using Ravers bank")

    elif cabletv_options == 2:
        print(input("Please enter an amount"))
        print("Processing...")
        print("Successfull")
        print("Thanks for using Ravers bank")

    elif cabletv_options == 3:
        print(input("Please enter an amount"))
        print("Processing...")
        print("Successfull")
        print("Thanks for using Ravers bank")

    else:
        print("Invalid options selected")

def electricity():
    """Electricity payment"""
    print(input("Please select an amount"))
    print("Processing...")
    print("Thanks for using Ravers bank")

def water():
    """Payment of water bills"""
    print(input("Please enter an amount"))
    print("Processing...")
    print("Thanks for using Ravers bank")

def airtime():
    """Payments of airtime"""
    print(input("Please enter an amount"))
    print("Processing...")
    print("Thanks for using Ravers bank")

def complaint():
    """Complaint of bank related issue"""
    print(input("Please enter your complaint: \n"))
    print("Complaint Received. We will get back in with you shortly")
    print("Thanks for using Ravers bank")

def generating_account_number():
    """Generating account number using the imported random"""

    return random.randrange(1111111111,9999999999)

init()
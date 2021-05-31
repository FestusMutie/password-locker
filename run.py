import random
from user import User
from Credentials import Credentials


def main():
    while True: 
        print("You have successfully joined password locker")  
        print('\n')
        print("select an abbreviation to navigate the program:for a new user pick 'nu':To login into your account 'lgn' or 'ext' to exit")
        abbreviated_word = input().lower() 
        print('\n')

        if abbreviated_word == 'nu':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()

            while confirm_password != created_user_password:
                print('This password is invalid!')
                print('enter the correct password!')
                created_user_password = input()
                print('confirm your password')
                confirm_password = input()

            else:
                print(f"congratulations{created_user_name}!your account has been successfully created!")
                print('\n')
                print("proceed to login")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print("invalid username or password")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()

            else:
                print(f"welcome: {entered_username} to your account")
                print("\n")

        elif abbreviated_word == 'lgn':
            print("welcome")
            print("Enter your user name") 
            default_user_name = input()

            print("Enter password")
            default_user_password =input()
            print('\n')
            while default_user_name != 'testuser' or default_user_password != '09876':
                print("wrong userName or password.Username 'testuser' and password '09876'")
                print("Enter user name")
                default_user_name = input()

                print("Enter password")
                default_user_password = input()
                print("\n")
            else:
                print("login success")
                print('\n')
                print('\n')

        elif abbreviated_word == 'ext': 
            break
        else:
            print("Enter a valid password to continue")  

if __name__ == '__main__':
    main()

        
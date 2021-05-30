import random
from user import User


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
                print('invalid password did not match!')
                print('enter your password')
                created_user_password = input()
                print('confirm your password')
                confirm_password = input()

        
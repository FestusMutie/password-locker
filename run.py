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

        
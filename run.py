#!/usr/bin/env python3.8
from user import User


def create_account(aname, username, password):
    '''
    Function to create user account details
    '''
    new_account_details = User(aname, username, password)
    return new_account_details


def save_user_account(user):
    '''
    Function to save contact
    '''
    user.save_user_account()


def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_user_accounts()


def main():
    print('Hello Welcome to password locker app. What is your name')
    user_name = input()

    print(f'Hello {user_name}. What would you like to do?')
    print('\n')


if __name__ == '__main__':
    main()

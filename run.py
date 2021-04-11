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
    print('Hello Welcome to password locker app. What is your name?')
    user_name = input()

    print(f'Hello {user_name}. What would you like to do?')
    print('\n')

    while True:
        print('Use thes short codes: cu - create new account, da - display accounts')

        short_code = input().lower()

        if short_code == 'cu':
            print('New account')
            print('-' * 10)

            print('Account Name eg. facebook, twitter etc')
            a_name = input()

            print('User name ...')
            u_name = input()

            print('Password ...')
            password = input()

            # create and save user account details
            save_user_account(create_account(a_name, u_name, password))
            print('\n')
            print(f'New {a_name} account created for {u_name} ')


if __name__ == '__main__':
    main()

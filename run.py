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
    Function to save account
    '''
    user.save_user_account()


def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return User.display_user_accounts()


def check_existing_account(account_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.account_exist(account_name)


def main():
    print('Hello Welcome to password locker app. What is your name?')
    user_name = input()

    print(f'Hello {user_name}. What would you like to do?')
    print('\n')

    while True:
        print('Use thes short codes: cu - create new account, da - display accounts, li - login ex - exit')

        short_code = input().lower()

        if short_code == 'cu':
            print('New account')
            print('-' * 10)

            print('Account Name eg. facebook, twitter etc')
            a_name = input()

            print('User name ...')
            u_name = input()

            print(
                'Enter password or generate password.')

            password = input()

            # create and save user account details
            save_user_account(create_account(a_name, u_name, password))
            print('\n')
            print(f'New {a_name} account created for {u_name} ')

        elif short_code == 'li':
            print('Enter account name')
            a_name = input()

            if check_existing_account(a_name):
                print('Enter username')
                u_name = input()
                print('Enter password or generate password.')

            else:
                print('That account does not exist')
        elif short_code == 'da':

            if display_accounts():
                print('Here is a list of all your account credentials')
                print('\n')

                for user in display_accounts():
                    print(f'{user.account} {user.user_name} {user.password}')

        elif short_code == 'ex':
            print('Bye ...')
            break

        else:
            print("I really didn't get that. Please use the short codes.")


if __name__ == '__main__':
    main()

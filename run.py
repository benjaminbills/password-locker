#!/usr/bin/env python3.8
from user import User
import string
import secrets
import pyperclip


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
    Function that check if a account name exists with that account name and return a Boolean
    '''
    return User.account_exist(account_name)


def find_account(account_name, user_name, password):
    '''
    Function that finds an account by account_name, user-name and password and returns the account
    '''
    return User.find_by_details(account_name, user_name, password)


def generate_password(ps_length):
    '''
    Function that generate password
    '''
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(ps_length))
    return password


def check_credentials(account_name, user_name, password):
    return User.check_credentials(account_name, user_name, password)


def copy_to_clipboard(account):
    return User.copy_details(account)


def main():
    print('Hello Welcome to password locker app. What is your name?')
    user_name = input()

    print(f'Hello {user_name}. What would you like to do?')
    print('\n')

    while True:
        print('Use thes short codes: \n ca - create new account, \n da - display accounts, \n li - login, \n cc - copy to clipboard \n ex - exit')

        short_code = input().lower()

        if short_code == 'ca':
            print('New account')
            print('==' * 25)

            print('Account Name eg. facebook, twitter etc:')
            print("Enter Account Name")
            a_name = input()

            print('Enter User name')
            u_name = input()

            print(
                'Enter password or generate password.')
            print('Use short code: \n ep - enter password \n gp - generate password')

            short_code = input().lower()
            if short_code == 'gp':
                print('Enter length of password')
                print('Your password length cannot be less than 5')
                print(
                    'If you enter any number less than 5 app will use default password length of 5')
                ps_length = int(input())
                if ps_length < 5:
                    password = generate_password(5)
                else:
                    password = generate_password(ps_length)
                save_user_account(create_account(a_name, u_name, password))
                print('\n')
                print(f'New {a_name} account created for {u_name} ')
            elif short_code == 'ep':
                print('Enter password...')
                password = input()
                # create and save user account details
                save_user_account(create_account(a_name, u_name, password))
                print('\n')
                print(f'New {a_name} account created for {u_name} ')
            else:
                print(
                    'please enter the short code to generate password -gp or enter password')

        elif short_code == 'li':
            print('Enter account name')
            a_name = input()

            if check_existing_account(a_name):
                print('Enter username')
                u_name = input()
                print('Enter password')

                password = input()
                if check_credentials(a_name, u_name, password):
                    search_account = find_account(a_name, u_name, password)
                    print(
                        f'You have succefully logged in to your {search_account.account} account')
                    print('==' * 25)
                else:
                    print('Incorrect password or user name')
            else:
                print('That account does not exist')
        elif short_code == 'da':

            if display_accounts():
                print('Here is a list of all your account credentials')
                print('\n')

                for user in display_accounts():
                    print(f'{user.account} {user.user_name} {user.password}')
        elif short_code == 'cc':
            print('Enter account name you want to copy')
            account = input()
            if check_existing_account(account):
                copy_to_clipboard(account)
                print(pyperclip.paste())
                print('Successfully Copied...')
                print('==' * 25)
            else:
                print('Account does not exist')
        elif short_code == 'ex':
            print('Bye ...')
            break

        else:
            print("I really didn't get that. Please use the short codes.")


if __name__ == '__main__':
    main()

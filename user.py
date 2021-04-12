import pyperclip


class Credential:
    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password


class User(Credential):
    '''
    class that generates new instance of user
    '''

    user_account_list = []

    def save_user_account(self):
        '''
        save user method saves a new user objects to the user_list
        '''
        User.user_account_list.append(self)

    @classmethod
    def display_user_accounts(cls):
        '''
        method that returns the user account list
        '''
        return cls.user_account_list

    @classmethod
    def account_exist(cls, account_name):
        '''
        Method that checks if an account exists from the user account list.
        Args:
            account name: account name to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_account_list:
            if user.account == account_name:
                return True

    @classmethod
    def find_by_details(cls, account, user_name, password):
        '''
        Method that takes in account details and returns an account that matches that the given details.
        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_account_list:
            if user.account == account and user.user_name == user_name and user.password == password:
                return user

    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in account details and returns an account that matches that the given details.
        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_account_list:
            if user.account == account:
                return user

    @classmethod
    def check_credentials(cls, account_name, user_name, password):
        '''
        Method that checks if user credential is correct for authentication from the user account list.
        Args:
            account_name, user_name, passsword
        Returns :
            Boolean: True or false depending if the details is correct
        '''
        for user in cls.user_account_list:
            if user.account == account_name and user.user_name == user_name and user.password == password:
                return True

    @classmethod
    def copy_details(cls, account):
        user_found = User.find_by_account(account)
        # uncomment the code to test copy to clip board
        # pyperclip.copy(user_found.user_name)
        # comment the below code
        pyperclip.copy(
            f'account:{user_found.account} \n username:{user_found.user_name} \n password:{user_found.password}')

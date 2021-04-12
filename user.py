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

class Credential:
    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password


class User(Credential):
    '''
    class that generates new instance of user
    '''

    user_list = []

    def save_user(self):
        '''
        save user method saves a new user objects to the user_list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user_accounts(cls):
        '''
          method that returns the contact list
          '''
        return cls.user_list

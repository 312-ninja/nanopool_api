import requests
from datetime import datetime
from datetime import timedelta


class NanoPool:
    def __init__(self, account):
        self.last_pull = 0
        self.account = account
        self.info = None
        self.get_general_info()
        
    def get_general_info(self):
        """
        Pulls the account information from remote API
        
        :return: None
        """
        
        self.last_pull = datetime.utcnow()
        url = 'https://api.nanopool.org/v1/eth/user/{}'.format(self.account)
        self.info = requests.get(url=url).json()

    def get_balance(self):
        """
        Gets account balance
        
        :return: str
        """
        
        self.refresh_info()
        return self.info['data']['balance']
    
    def refresh_info(self):
        """
        Refreshes account information only if
        last pull was more than 5 minutes ago
        
        :return: None
        """
        
        if self.last_pull + timedelta(minutes=5) < datetime.utcnow():
            self.get_general_info()
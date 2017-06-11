import requests


class NanoPool:
    def __init__(self, account):
        self.account = account

    def get_balance(self):
        url = 'https://api.nanopool_api.org/v1/eth/balance/{}'.format(self.account)
        r = requests.get(url=url)
        return r.json()['data']

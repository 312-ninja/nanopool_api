#! venv/bin/python3

from api import NanoPool

import configparser


config = configparser.ConfigParser()

config.read('config')

address = config['ACCOUNT']['address']

nanopool = NanoPool(address)

print(nanopool.info)

print(nanopool.get_balance())

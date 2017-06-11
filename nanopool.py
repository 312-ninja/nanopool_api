#! venv/bin/python3

from api import NanoPool

address = input('Account Address: ')

nanopool = NanoPool(address)

print(nanopool.get_balance())

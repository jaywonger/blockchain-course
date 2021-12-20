# use the commands below to get it working
#python3 -m venv env 
#source env/bin/activate
#pip3 install py-solc-x

from solcx import compile_standard
from web3 import Web3
from dotenv import load_dotenv

import json
import os

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    #print(simple_storage_file)
    
# Compile our solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x9eEE551a3159A165fB016c2D3569f55B1c5db895"
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get latest transaction 
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print(signed_txn)

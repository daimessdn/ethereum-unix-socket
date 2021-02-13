# import libraries
from web3 import Web3

# init'd Web3 instance to infura URL
## add Infura URL with Rinkeby testnet endpoint
infura_url = "https://rinkeby.infura.io/v3/5305a065632e4688b0f97c021bc6aac2"
web3 = Web3(Web3.HTTPProvider(infura_url))

# testing web3 operations
## get current block number
bn = web3.eth.blockNumber
print(bn)

## get current balance for specific address
bl = web3.eth.getBalance("0xACa20B87dAEFe8a89f80E15493609bE116c8efc5")
print(bl)
# import libraries
import json
from web3 import Web3

# init'd Web3 instance to infura URL
## add Infura URL with Rinkeby testnet endpoint
infura_url = "https://rinkeby.infura.io/v3/5305a065632e4688b0f97c021bc6aac2"
web3 = Web3(Web3.HTTPProvider(infura_url))

# init'd credentials
## init'd sender wallet address
sender_address = "0xACa20B87dAEFe8a89f80E15493609bE116c8efc5"

## get sender private key from a hidden file
with open('.%s.txt' % sender_address, "r") as f:
    sender_private_key = f.read()

## init'd receiver address
receiver_address = "0xd51e18D83C0e4EeB3D62716eA78Dcc0eB4038a7a"

tx_file = open("transaction_input.json", )
tx_json = json.load(tx_file)
tx_file.close()

print(tx_json)

# # transcation using Ethereum
# ## get transaction count
# transaction_count = web3.eth.getTransactionCount(sender_address)

# # create transactions
# transactions = []

# for index, item in enumerate(tx_json):
#     transactions.append({
#         "nonce": web3.eth.getTransactionCount(sender_address)
#         "to": item["to_address"],
#         "value": int(item["amount"], 0),
#         "gas": 200000,
#         "gasPrice": 1000000000
#     })

# for index, tx in enumerate(transactions):
#     signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)
#     sent_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#     print(web3.toHex(sent_hash))

# print(transactions)

# ## signed the transaction we've just created
# signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)

# # print(signed_tx.rawTransaction.hex())
# # print(signed_tx.hash.hex())

# ## send signed transaction to be proceed
# sent_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(sent_hash)
# print(web3.toHex(sent_hash))
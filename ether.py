# import libraries
from web3 import Web3

# init'd Web3 instance to infura URL
## add Infura URL with Rinkeby testnet endpoint
infura_url = "https://rinkeby.infura.io/v3/5305a065632e4688b0f97c021bc6aac2"
web3 = Web3(Web3.HTTPProvider(infura_url))

# init'd credentials
## init'd sender wallet address
sender_address = "0xACa20B87dAEFe8a89f80E15493609bE116c8efc5"

## get sender private key from a hidden file
f = open('.%s.txt' % sender_address, "r")
sender_private_key = f.read()
f.close()

print(sender_private_key)

## init'd receiver address
receiver_address = "0xd51e18D83C0e4EeB3D62716eA78Dcc0eB4038a7a"

# # testing web3 operations
# ## get current block number
# bn = web3.eth.blockNumber
# print(bn)

# ## get current balance for specific address
# bl1 = web3.eth.getBalance(sender_address)
# bl2 = web3.fromWei(bl1, "ether")

# print(bl1, bl2)

## get transaction count
gtc = web3.eth.getTransactionCount(sender_address)
print(gtc)

# create transaction
tx = {
    "nonce": gtc,
    "to": receiver_address,
    "value": web3.toWei(0.001, "ether"),
    "gas": 200000,
    "gasPrice": web3.toWei(20, "gwei")
}

## signed the transaction we've just created
signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)

# print(signed_tx)

# print(signed_tx.rawTransaction.hex())
# print(signed_tx.hash.hex())

## send signed transaction to be proceed
sent_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(sent_hash)
print(web3.toHex(sent_hash))
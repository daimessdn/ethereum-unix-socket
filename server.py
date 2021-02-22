#!/usr/bin/env python3

# import libraries
from web3 import Web3
import socket
import sys
import os
import json

# init'd Web3 instance to infura URL
## add Infura URL with Rinkeby testnet endpoint
infura_url = "https://rinkeby.infura.io/v3/5305a065632e4688b0f97c021bc6aac2"
web3 = Web3(Web3.HTTPProvider(infura_url))

def generate_private_key(address):
    """
    Generate private key of address using file
    with the same address name
    """
    with open(".%s.txt" % address, "r") as f:
       private_key = f.read()

    return private_key

def estimate_gas(tx):
    """
    Get estimated gas usage
    """

    return web3.eth.estimateGas(tx)

# define function for create and sign transaction
def make_signed_tx(data, entry):
    """
    Function for construct and sign transaction
    input: dict:data (id, type, from_address, to_address, amount)
    output: dict:data (id, tx)
    """
    data = json.loads(data)

    # init'd transaction
    ## redefined the Ethereum value into wei standard
    ## in each parameter. gas and gasPrice are assumed to be fixed value
    gas_usage = web3.toWei(0.002, "gwei")
    gas_price = web3.toWei(1, "gwei")
    tx_value = web3.toWei(data["amount"], "ether") # eth amount to wei

    ## applied the value conversion in tx dictionary
    tx = {
        "from": data["from_address"],
        "to": data["to_address"],
        "value": tx_value,
        "gas": gas_usage,
        "gasPrice": gas_price,
        "nonce": web3.eth.getTransactionCount(data["from_address"]) + entry
    }

    # resolved tx value by fee subtraction
    tx_fee = (estimate_gas(tx) * web3.eth.gasPrice)
    tx["value"] -= tx_fee

    # get the signed transaction
    signed_tx = web3.eth.account.signTransaction(tx, generate_private_key(tx["from"]))

    # return id and transaction object 
    return { "id": data["id"], "tx": web3.toHex(signed_tx.rawTransaction) }

# init'd empty connection and client node
conn, client = None, None

# init'd initial nonce entry by 0
## assuming all signed tx will not be broadcasted yet,
## it will be +1 for every single entry
nonce_entry = 0

try:
    # get a pathname variable from second argument of program
    pathname = sys.argv[1]

    # delete the old socket before creating a new socket
    if (os.path.exists(pathname)):
        os.remove(pathname)

    # create a new socket for server
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # bind the socket into pathname
    ## and make socket listening to incoming client
    s.bind(pathname)
    print("Creating socket with pathname: %s" % pathname)
    s.listen(1)

    # waiting for incoming client
    print("\nWaiting for connection...")
    while True:
        # accepting incoming client
        ## if the client is not connected yet
        if (not conn and not client):
            conn, client = s.accept()
            print("Connected to client.")

            # restart the nonce entry
            nonce_entry = 0
            print("Entry restart from 0 and will be added by nonce.")
            
        # interaction with client
        else:
            # receiving transaction from client
            ## init'd empty data
            data = ""
            data_reading = True

            ## reading received data until there are no data
            while data_reading:
                data_recv = conn.recv(64).decode("utf-8")
                data += data_recv

                if (len(data_recv) < 64):
                    data_reading = False

                # print(data)
            print("\n" in data)

            if ("" != data):
                print("\nGetting data from client. Signing a transaction...")

                # convert data into dictionary
                ## then construct a signed transaction
                ## to be sent to client
                json_data = json.loads(data)
                signed_tx_data = make_signed_tx(json_data, nonce_entry)

                # sending signed transaction to client
                print("Transcation signed and has been sent into client. Ready to receive a next input...")
                conn.sendall(json.dumps(signed_tx_data).encode("utf-8"))

                # next entry will be +1
                nonce_entry += 1

            # in case if client is disconneted
            else:
                conn.close()
                conn, client = None, None
                print("\nConnection closed. Waiting for incoming client...")

# in case the arguments is not valid
except IndexError:
    print("Invalid argument (\033[93m\33[1m<pathname>\33[0m\33[0m value required)")

    print("\nIt should be")
    print("python3 server.py \033[93m\33[1m<pathname>\33[0m\33[0m")
    
    print("\nor")
    print("./vault \033[93m\33[1m<pathname>\33[0m\33[0m")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Shutting down server.")
    if (None != conn and None != client):
        conn.close()

    os.remove(pathname)

finally:
    if (None != conn and None != client):
        conn.close()

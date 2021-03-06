#!/usr/bin/env python3

# import libraries
import socket
import sys
import os
import json

def get_txs_input():
    # get transaction input
    ## when the blank entry is pressed, all txs will be sent into server.
    data_input = True
    data = ""

    print("\nInput transaction (type blank for terminate):")
    while data_input:
        data_preinput = str(input(">> "))

        if (data_preinput == ""):
            data_input = False
        else:
            data += json.dumps(data_preinput) + "\n"

    return data

def recv_signed_tx():
    """
    Receives all signed transactions from server
    """

    # receiving signed transaction
    ## init'd empty data
    signed_tx = ""
    data_reading = True

    ## reading received signed_tx until there are no data
    while data_reading:
        data_recv = s.recv(180).decode("utf-8")
        signed_tx += data_recv

        if (len(data_recv) < 180):
            data_reading = False

    return signed_tx

try:
    # get a pathname variable from second argument of program
    pathname = sys.argv[1]

    if (os.path.exists(pathname)):
        # create a new socket for server
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # connecting socket into existing socket with specific path
        print("Connected to socket with pathname: %s" % pathname)

        # begin connection with server
        s.connect(pathname)
        connection_loop = True
        while connection_loop:
            transactions = get_txs_input()

            # if the input is not empty,
            ## it will send all data transactions to server
            if ("" != transactions):
                # sending data input
                s.sendall(transactions.encode("utf-8"))

                print("\nAll transactions sent to server. Waiting for signed transactions received...\n")

                # looping process to receive all signed transactions
                recv_loop = True
                while recv_loop:
                    signed_tx = recv_signed_tx()

                    # checking for 'SUCCESS!' signal for stop receiving messages
                    if (signed_tx != "SUCCESS!"):
                        print("<< %s" % signed_tx)
                    else:
                        recv_loop = False

                print("\nReady for the next transactions input...")

            # terminated connection if there are no data input
            else:
                print("Shutting down...")
                connection_loop = False

# in case the arguments is not valid
except IndexError:
    print("Invalid argument (\033[93m\33[1m<pathname>\33[0m\33[0m value required)")

    print("\nIt should be")
    print("python3 server.py \033[93m\33[1m<pathname>\33[0m\33[0m")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Done.")

# connection not found case
except ConnectionRefusedError:
    print("Connection not exists, exiting program...")

#!/usr/bin/env python3

# import libraries
import socket
import sys
import os
import json

txs = []

try:
    # get a pathname variable from second argument of program
    pathname = sys.argv[1]

    if (os.path.exists(pathname)):
        # create a new socket for server
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # connecting socket into existing socket with specific path
        print("Connecting to socket with pathname: %s" % pathname)
        s.connect(pathname)

        while True:
            # get transaction input
            data = str(input("\n>> "))

            # if the input is not empty,
            ## it will send data in JSON to the server
            if ("" != data):
                data = json.dumps(data)
                s.send(data.encode("utf-8"))

                signed_tx = s.recv(1024)
                print("<< %s" % signed_tx.decode('utf-8'))
            
            else:
                print("Shutting down...")
                break

# in case the arguments is not valid
except IndexError:
    print("Invalid argument (\033[93m\33[1m<pathname>\33[0m\33[0m value required)")

    print("\nIt should be")
    print("python3 server.py \033[93m\33[1m<pathname>\33[0m\33[0m")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Done.")

except ConnectionRefusedError:
    print("Connection not exists, exiting program...")

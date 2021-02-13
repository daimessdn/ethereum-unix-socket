# import libraries
import socket
import sys
import os

# init'd empty connection and client node
conn, client = None, None    

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
            
        # interaction with client
        else:
            data = conn.recv(1024)

            if ("" != data.decode("utf-8")):
                print("Getting data from client: %s" % data.decode("utf-8"))

            # in case if client is disconneted
            else:
                conn.close()
                conn, client = None, None
                print("\nConnection closed. Waiting for another client...")

# in case the arguments is not valid
except IndexError:
    print("Invalid arguments (need <pathname> value)")
    print("$ python3 server.py <pathname>")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Shutting down server.")
    if (None != conn and None != client):
        conn.close()

    os.remove(pathname)

finally:
    if (None != conn and None != client):
        conn.close()
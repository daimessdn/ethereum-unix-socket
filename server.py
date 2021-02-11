# import libraries
import socket
import sys
import os

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

    conn, client = None, None    

    # waiting for incoming client
    print("\nWaiting for connection...")
    while True:
        # accepting incoming client
        if (not conn and not client):
            conn, client = s.accept()
            print("Connected to client.")
        else:
            data = conn.recv(1024)

            if ("" != data.decode("utf-8")):
                print("Getting data from client: %s" % data.decode("utf-8"))
            else:
                conn.close()
                conn, client = None, None

# in case the arguments is not valid
except IndexError:
    print("Invalid arguments (need <pathname> value)")
    print("$ python3 server.py <pathname>")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Shutting down server.")
    conn.close()

finally:
    conn.close()
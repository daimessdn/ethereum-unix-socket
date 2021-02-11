# import libraries
import socket
import sys
import os

print(sys.argv[1])

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
    while True:
        # accepting incoming client
        conn, client = s.accept()

        data = conn.recv(1024)
        print("Getting data from client: %s" % data)

# in case the arguments is not valid
except IndexError:
    print("Invalid arguments (need <pathname> value)")
    print("$ python3 server.py <pathname>")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Shutting down server.")
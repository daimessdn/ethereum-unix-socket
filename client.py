# import libraries
import socket
import sys
import os

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
            data = str(input("> "))

            if ("" != data):
                s.send(data.encode("utf-8"))
            
            else:
                break

# in case the arguments is not valid
except IndexError:
    print("Invalid arguments (need <pathname> value)")
    print("$ python3 client.py <pathname>")

# exiting program by keyboard input
except KeyboardInterrupt:
    print("Done.")

except ConnectionRefusedError:
    print("Connection not exists, exiting program...")

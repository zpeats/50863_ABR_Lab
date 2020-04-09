import socket
from bsonrpc import JSONRpc
import time
import bsonrpc

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6000))

rpc = JSONRpc(s)

def main():
    while(1):
        time.sleep(2)
        print('sending req')
        result = rpc.invoke_request("swapper",'hello world')
        # Execute in server:
        # "!dlroW olleH"
        print(result)
        time.sleep(5)

    rpc.close()  # Closes the socket 's' also


if __name__ == "__main__":
    main()
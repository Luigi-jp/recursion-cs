import os
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './tmp/socket_file'

try:
    sock.connect(server_address)
    print('Connected to Server')
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    user_input = input('Enter a message: ')
    sock.sendall(user_input.encode())

    sock.settimeout(5)

    try:
        while True:
            data = sock.recv(4096)
            if data:
                print('Server response: ', data.decode('utf-8'))
            else:
                break
    except(TimeoutError):
        print('socket timeout, ending listening for server messages')

finally:
    print('Closing socket')
    sock.close()

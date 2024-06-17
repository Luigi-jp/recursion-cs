import json
import math
import socket
import os

def floor(x):
    return math.floor(x)

def nroot(n, x):
    return x ** (1 / n)

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(strArr):
    return sorted(strArr)

functions = {
    'floor': floor,
    'nroot': nroot,
    'reverse': reverse,
    'validAnagram': validAnagram,
    'sort': sort
}

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()

    try:
        while True:
            data = connection.recv(4096)
            if data:
                request = json.loads(data.decode('utf-8'))
                connection.sendall(data)
            else:
                break

    finally:
        connection.close()
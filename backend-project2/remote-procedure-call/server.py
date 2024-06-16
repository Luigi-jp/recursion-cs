import socket
import os

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
                # jsonデータが受け取れるか確認
                print(data.decode('utf-8'))
                connection.sendall(data)
            else:
                break

    finally:
        connection.close()
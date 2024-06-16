from faker import Faker
import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)

sock.listen(1)

while True:
    # connection: 接続したクライアントと通信するための新しいソケットオブジェクト
    # sockは引き続き別のクライアントからの接続を待ち受けるために使用され、connectionは個別のクライアントと通信するために使用される
    # client_address: 接続したクライアントのアドレス
    connection, client_address = sock.accept()

    try:
        while True:
            data = connection.recv(4096)
            data_str = data.decode('utf-8')
            print('Received ', data_str)

            if data:
                faker = Faker()
                response = faker.text()
                connection.sendall(response.encode())
            else:
                break

    finally:
        print('Closing {} connection'.format(client_address))
        connection.close()
import json
import math
import socket
import os

def floor(x):
    return math.floor(x)

def nroot(n, x):
    return math.floor(x ** (1 / n))

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

def connection():
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

                    try:
                        result = handle_request(request)
                        response = create_response(result)
                        connection.sendall(response.encode())
                    except Exception as error:
                        response = create_error_response(error)
                        connection.sendall(response.encode())
                else:
                    break

        finally:
            connection.close()

def handle_request(request):
    try:
        result = functions[request['method']](*request['params'])
        return result
    except Exception as error:
        raise error

def create_response(result):
    response = {
        "results": result,
        "result_type": type(result).__name__,
        "id": 1
    }
    return json.dumps(response)

def create_error_response(error):
    response = {
        "error": {
            "message": str(error)
        },
        "id": 1
    }
    return json.dumps(response)

def main():
    connection()

if __name__ == '__main__':
    main()
import socket
from random import random

from Crypto.Cipher import AES

"""
    Jakub Kowalewski
"""


def client_program():
    key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
    aes = AES.new(key, AES.MODE_CBC, iv)

    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    message = aes.encrypt(message)
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

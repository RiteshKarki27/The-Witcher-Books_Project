import socket
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"connection to {adr} established")
    clt.send(bytes('Welcome to the server', 'utf-8'))

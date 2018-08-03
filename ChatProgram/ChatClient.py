from socket import *
from threading import Thread
import sys

HOST = 'localhost'
PORT = 33000
BUFSIZE = 2048
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

def recv():
    while True:
        data = str(tcpCliSock.recv(BUFSIZE).decode('utf-8'))
        print(data)

Thread(target=recv).start()
while True:
    data = input('> ')
    if data == '{quit}' :
        tcpCliSock.send(bytes(data, 'utf-8'))
        tcpCliSock.close()
    else:
        tcpCliSock.send(bytes(data, 'utf-8'))


tcpCliSock.close()

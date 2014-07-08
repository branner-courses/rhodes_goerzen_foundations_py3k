#!/usr/bin/env python
# Rhodes and Goerzen, Foundations of Python Network Programming - Chapter 5
# blocks.py
# Sending data one block at a time.
# Converted to Python3 by David Branner, 20140708.

import socket, struct, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = sys.argv.pop() if len(sys.argv) == 3 else '127.0.0.1'
PORT = 1060
frmat = struct.Struct('!I') # for messages up to 2**32 - 1 in length

def recvall(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('socket closed {} bytes into a {}-byte message'.
                    frmat(len(data), length))
        data += more
    return data

def get(sock):
    lendata = recvall(sock, format.size)
    (length,) = frmat.unpack(lendata)
    return recvall(sock, length)

def put(sock, message):
    sock.send(frmat.pack(len(message)) + message)


if sys.argv[1:] == ['server']:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print('Listening at {}'.format(s.getsockname()))
    sc, sockname = s.accept()
    print('Accepted connection from {}'.format(sockname))
    sc.shutdown(socket.SHUT_WR)
    while True:
        message = get(sc)
        if not message:
            break
        print('Message says: {}'.format(message.encode('utf-8')))
    sc.close()
    s.close()

elif sys.argv[1:] == ['client']:
    s.connect((HOST, PORT))
    s.shutdown(socket.SHUT_RD)
    put(s, b'Beautiful is better than ugly.\n')
    put(s, b'Explicit is better than implicit.\n')
    put(s, b'Simple is better than complex.\n')
    put(s, '')
    s.close()

else:
    sys.stederr.write('usage: blocks.py server|client [host]')

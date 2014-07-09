#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2
# udp_local.py
# UDP client and server on localhost
# Converted to Python3 by David Branner, 20140708, works.

import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

if sys.argv[1:] == ['server']:
    s.bind(('127.0.0.1', PORT))
    print('Listening at {}'.format(s.getsockname()))
    while True:
        data, address = s.recvfrom(MAX)
        print('The client at {} says {}'.
                format(address, str(data, 'utf-8')))
        s.sendto(bytes('Your data was {} bytes'.format(len(data)), 'utf-8'),
                address)

elif sys.argv[1:] == ['client']:
    print('Address before sending: {}'.format(s.getsockname()))
    s.sendto(b'This is my message', ('127.0.0.1', PORT))
    print('Address after sending: {}'.format(s.getsockname()))
    data, address = s.recvfrom(MAX) # overly promiscuous - see text!
    print('The server {} says {}'.
            format(address, str(data, 'utf-8')))

else:
    sys.stderr.write('usage: udp_local.py server|client')

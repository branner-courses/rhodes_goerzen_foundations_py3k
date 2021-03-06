#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2
# big_sender.py
# Send a big UDP packet to our server.
# Converted to Python3 by David Branner, 20140709, works on Ubuntu 14.04.
# DOES NOT WORK ON OS 10.9: `IN.IP_MTU_DISCOVER` is not found in Python 3.

import IN, socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

if len(sys.argv) != 2:
    sys.stderr.write('usage: big_sender.py host\n')
    sys.exit(2)

hostname = sys.argv[1]

s.connect((hostname, PORT))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
try:
    s.send(b'#' * 65000)
except OSError:
    print('The message did not make it')
    option = getattr(IN, 'IP_MTU', 14) # constant taken from <linux/in.h>
    print('MTU: {}\n'.format(s.getsockopt(socket.IPPROTO_IP, option)))
else:
    print('The big message was sent! Your network supports really big packets!')

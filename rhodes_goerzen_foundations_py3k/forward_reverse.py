#!/usr/bin/env python
# Rhodes and Goerzen, Foundations of Python Network Programming - Chapter 4
# forward_reverse.py
# Checking whether a hostname works both forward and backward.
# Converted to Python3 by David Branner, 20140709, works.

import socket, sys

if len(sys.argv) != 2:
    sys.stderr.write('usage: forward_reverse.py <hostname>\n')
    sys.exit(2)
hostname = sys.argv[1]
try:
    infolist = socket.getaddrinfo(
        hostname, 0, 0, socket.SOCK_STREAM, 0,
        socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
        )
except socket.gaierror as e:
    print('Forward name service failure: {}'.format(e.args[1]))
    sys.exit(1)
info = infolist[0] # choose the first, if there are several addresses
canonical = info[3]
socketname = info[4]
ip = socketname[0]
if not canonical:
    print('WARNING! The IP address {} has no reverse name'.format(ip))
    sys.exit(1)
print('{} has IP address {}'.format(hostname, ip))
print('{} has the canonical hostname {}'.format(ip, canonical))
# Lowercase for case-insensitive comparison, and chop off hostnames.
forward = hostname.lower().split('.')
reverse = canonical.lower().split('.')
if forward == reverse:
    print('Wow, the names agree completely!')
    sys.exit(0)

# Truncate the domain names, which now look like ['www', 'mit', 'edu'],
# to the same length and compare. Failing that, be willing to try a
# compare with the first element (the hostname?) lopped off if both of
# them are the same length.

length = min(len(forward), len(reverse))
if (forward[-length:] == reverse[-length:]
    or (len(forward) == len(reverse)
        and forward[-length+1:] == reverse[-length+1:]
        and len(forward[-2]) > 2)):
        # avoid thinking '.co.uk' means a match!
    print('The forward and reverse names have a lot in common')
else:
    print('WARNING! The reverse name belongs to a different organization')

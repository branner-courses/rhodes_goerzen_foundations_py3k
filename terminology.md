## Terminology

 * **connection name**, a 4-tuple of local and remote IP addresses and ports
 * **datagram**: "application-level block for transmitted data" (p. 20)
 * **deadlock**: the filling of a socket with more data than can ever be read, so that it hangs forever
 * **flow control**: adjustment of window by receiver, if input buffer is full or network appears noisy
 * **gateway machine**: connects local subnet to the rest of the Internet
 * **mask**: integer (multiple of 8) indicating how many of an IP address's most significant bits have to match to make a host belong to that subnet. E.g., `127.0.0.0/8` (represents `127.*.*.*`); `192.168.0.0/16` (represents `192.168.*.*`), etc.
 * **network interface**: hardware-software boundary; here, the IP address (including or without port)
 * **packet**: byte string, transmitted as a single unit between network devices; minimum features: byte-string data, an address
 * **passive socket**: contains just a socket name to which connections are not possible
 * **protocol stack**: "simpler network services are used as the foundation on which to build more sophisticated services"
 * **socket name**: the address and port where the server will listen
 * **window**: amount of unacknowledged data permitted at any moment
 
[end]
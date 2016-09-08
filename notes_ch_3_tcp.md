## Notes, Chapter 3 "TCP"

Second edition.

TCP is used for "stream" sockets, split into packets automatically.

### How TCP works

 * Protocols that carry documents and files nearly always ride atop TCP. ... It is rare that anyone but an expert in protocol design can improve upon the performance of a modern TCP stack. (p. 35)
 
 * Every packet has a sequence number representing the total number of bytes sent up to then. The initial number is ideally random, so that it is harder for attackers to forge packets. (p. 35)

 * Multiple packets can be sent before acknowledgement from the receiver. Term:
 
   * **window**: amount of unacknowledged data permitted at any moment
   * **flow control**: adjustment of window by receiver, if input buffer is full or network appears noisy

### When to use TCP

 * Cases where not optimum:
 
   * unwieldy where a single, small request only is sent to a server, with little likelihood of more requests soon after
   * inappropriate in audio, e.g., where lost packets aren't useful out of sequence; here, give head and tail of each packet redundant content from prior and following packets.

### What TCP sockets mean

 * Unlike UDP, TCP is stateful, so a persistent connection is needed. The client initiates the connection and the server creates a new socket.
 * The POSIX interface to TCP distinguishes "passive" sockets (containing **socket name**, the address and port where the server will listen but to which connections are not possible) from "connected" (active) sockets.
 * Multiple active sockets may all have the same socket name, but each has a different **connection name**, a 4-tuple of local and remote IP addresses and ports.

### A simple TCP client and server

 * choice of IP and port
 * differences from simple UDP client and server:
 
   * `connect()` can fail
   * client doesn't need to make provision for missing data; network stack will perform any needed re-transmission
   * `send()` and `recv()` do not transmit datagrams atomically — data may be subdivided and reassembled at the other end

 * `send()` may succeed completely, be blocked completely, or succeed in sending only part of the data; because of the latter, it is customary to place it in a `while` loop. `socket.socket.sendall()` is an optimized method that handles all three possibilities.
 * `recv()` has the same three possibilities as `send()`, but there is no comparable `socket.socket.recvall()` method; it is often necessary to process messages in order to know how much more is coming — the size of the full message is not specified at the beginning.

### One socket per conversation

 * Server: `socket.socket()`, `setsockopt()`, `bind()`, `listen()`, `accept()`, [`recv()`, `sendall()`], `close()`
 * Client: `socket.socket()`, `connect()`, `sendall()`, `recv()`, `close()`

### Address already in use

 * To prevent an address locking on interrupt, use `setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`. This affects only connected, not listening, sockets.
 * UNIX `setsockopt` man page has more information about these constants.

### Binding to interfaces

 * Empty IP address string (`""`) defaults to `0.0.0.0`, meaning "any interface".

### Deadlock

 * Each end of a TCP stack has an output buffer of finite size to prevent dropping packets that later have to be resent.
 * Client and server should answer or acknowledge each other's messages regularly, to prevent the buffers overflowing.

### Closed Connections, Half-Open Connections

 * When a socket is closed, it returns an empty string. (Not true for non-blocking sockets.)
 * Socket can be half-closed with `shutdown()`; no further reading, but replies are still possible. This is often used to create a uni-directional socket.

## Using TCP Streams Like Files

 * Python uses `send()`/`recv()` for sockets and restricts `write()`/`read()` to files. But `socket.makefile()` can create a socket object with file I/O-like methods: it is a `TextIOWrapper` layer over a `BufferedIOBase` object or buffer.

### Communication packets

 * `RST`: reset connection
 * `SYN`: initiated by `connect()`, leads to creation of socket in server
 * `FIN`: 
 * `ACK`: 
 * `FIN-ACK`: 
 * `SYN-ACK`: 

### Terms

 * datagram: "application-level block for transmitted data" (p. 20)
 * network interface: hardware-software boundary; here, the IP address (including or without port)
 * deadlock: the filling of a socket with more data than can ever be read, so that it hangs forever

[end]

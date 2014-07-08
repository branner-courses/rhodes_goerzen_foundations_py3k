## Rhodes-Goerzen Foundations, Py3K

Python 3 versions of code from Brandon Rhodes and John Goerzen's _Foundations of Python Network Programming_, Second Edition (New York: Apress, 2010).

### Current contents:

 * Listing 2–1. `udp_local.py`: UDP Server and Client on the Loopback Interface
 * Listing 2–2. `udp_remote.py`: UDP Server and Client on Different Machines
 * Listing 2–3. `big_sender.py`: Sending a Very Large UDP Packet (**note**: This program does not work as written on Mac OS 10.9.4; `IN.IP_MTU_DISCOVER` is not found in Python 3 on this system.)
 * Listing 2–4. `udp_broadcast.py`: UDP Broadcast
 * Listing 3–1. `tcp_sixteen.py`: Simple TCP Server and Client
 * Listing 3–2. `tcp_deadlock.py`: TCP Server and Client That Deadlock
 * Listing 4–1. `www_ping.py`: Using `getaddrinfo()` to Create and Connect a Socket
 * Listing 4–2.`forward_reverse.py`:  Confirming a Forward Lookup with a Reverse Lookup
 * Listing 4–3.`dns_basic.py`:  A Simple DNS Query Doing Its Own Recursion
 * Listing 4–4. `dns_mx.py`: Resolving an E-mail Domain Name
 * Listing 5–1. `streamer.py`: Sending a Single Stream of Data


 ----

 * Listing 9–1. `verbose_handler.py`: An HTTP Request and Response that Prints All Headers

### Changes from Python2 to Python3

 * `print >>sys.stderr, <str>` => `sys.stderr.write(<str>)`
 * `print` as function
 * string formatting with `<str>.format()`
 * sockets now send and receive strings as bytestring:
   * send: `'content'` => `b'content'`
   * after receiving: `repr(data)` => `data.encode('utf-8')`
 * some modules have changed:
   * `urllib2` => `urllib`, and the new module is organized differently 
   * `io`: `io.StringIO` => `io.BytesIO` because we are dealing with bytestring now
   * `pydns` => `py3dns`

[end]

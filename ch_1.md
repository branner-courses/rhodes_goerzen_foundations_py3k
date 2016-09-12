## Notes, Chapter 1 "Client/Server Networking"

Third edition.

TCP is used for "stream" sockets, split into packets automatically.

### The Building Blocks: Stacks and Libraries

 * **protocol stack**: "simpler network services are used as the foundation on which to build more sophisticated services"
 * `pygeocoder`: "clean interface to Google’s geocoding features" (not of Google origin). This library is "the top layer of a network stack".

### Application Layers

 * Using the `requests` HTTP library: one layer down from the top layer: using a protocol to construct a URL, fetch a response, parsing it as JSON.

### Speaking a Protocol

 * Using the HTTP protocol directly (`http.client` library).

### A Raw Network Conversation

 * Using `socket` to send and receive strings (including HTTP headers and data) across an IP network.

### Turtles All the Way Down

 * Example of a stack, each layer of which uses the tools of the next layer down:

   * Top-level is an API.
   * URLs name documents that can be retrieved using HTTP.
   * HTTP supports document-oriented commands such as GET using raw TCP/IP sockets.
   * TCP/IP sockets know how only to send and receive byte strings.

 * Python offers very complete tools wrapping multiple layers of this stack.
 * Explicitly lower-level coding tends to be uglier and risks more errors.
 * Higher-level protocols work by hiding lower-level layers. (Consider: does a higher-level library correctly hide errors at lower levels?)
 * Protocols lower than `socket` are:
 
   * TCP: manages packets as streams of bytes
   * IP: sends packets between computers
   * link layer: network hardware devices that can send physical messages between directly linked computers

### Encoding and Decoding (Py3K differs a lot from Py2 here)

 * `bytes.decode()` => `str`
 * `str.encode()` => `bytes`

### The Internet Protocol

 * **packet**: byte string, transmitted as a single unit between network devices
 * necessary properties of a packet: byte-string data, an address

### IP Addresses

 * special IP address ranges:
 
   * `127.*.*.*`. Note that `127.*.*.1` has the hostname `localhost`
   * private subnets: `10.*.*.*`, `172.16–31.*.*`, `192.168.*.*`

### Routing

 * **gateway machine**: connects local subnet to the rest of the Internet
 * **mask**: integer (multiple of 8) indicating how many of an IP address's most significant bits have to match to make a host belong to that subnet. E.g., `127.0.0.0/8` (represents `127.*.*.*`); `192.168.0.0/16` (represents `192.168.*.*`), etc.

### Packet Fragmentation

 * OS sets `DF` ("don't fragment") flag to preclude efficient variation in packet-length — done with TCP; not done with UDP.
 * `DF` flag caused problems in the era of `PPPoE`. "Illustrates how a low-level IP feature can generate user-visible symptoms."
 * Packets may also be fragmented if too large for a hop between routers along its path.

[end]

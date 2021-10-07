# Python Socket Programming

This project is a small effort to demonstrate and teach myself the basics of socket programming in python


## Echo Server

Simple TCP listener. This creates a socket, binds, listens and accepts connections on a hard-coded address and port. It echos whatever string it receives. Sending 'exit' will kill the server. Test it out with `nc [address] [port]` 

## ICMP Sniffer

This script sniffs ICMP traffic with raw sockets. Then it decodes the IP header and compares the source IP to the loopback address. Throws an alert if the source is not the loopback. This is a pseudo IDS and would be interesting to use scapy and iptables to actually mangle packets and perhaps drop them if they meet rule criteria 
#!/usr/bin/python3

import socket
from struct import unpack
from ipaddress import ip_interface

def main():
    icmp_sock=socket.socket(family=socket.AF_INET,type=socket.SOCK_RAW,proto=socket.IPPROTO_ICMP)
    print('sniffing icmp')
    while(True):
        packet,remote_addr=icmp_sock.recvfrom(65535)
        ip_header=packet[:20]
        icmp_header=packet[20:28]
        #https://en.wikipedia.org/wiki/IPv4#Header
        ver_header_length, tos, total_length, ident, flags_frag, ttl, data_proto, checksum, s_ip, d_ip  =unpack('! B B H H H B B H 4s 4s', ip_header)
        #TODO bitwise math to split the sub-byte header fields like version and fragmentation flags
        source_ip = '.'.join([str(oct) for oct in s_ip])
        dest_ip = '.'.join([str(oct) for oct in d_ip])
        loopback=ip_interface('127.0.0.1')
        source_addr=ip_interface(source_ip)
        #alert on icmp from remote systems
        if loopback!=source_addr and data_proto == 1:
            icmp_type, icmp_code, checksum, rest_of_header = unpack('! B B H 4s', icmp_header)
            print(f'ALERT: remote ICMP detected from {source_ip} to {dest_ip}. Type is {icmp_type} and code is {icmp_code}')


if __name__=='__main__':
    main()
#!/usr/bin/python3

import socket
import sys

def main():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        host='127.0.0.1'
        port=4444
        s.bind((host,port))
        listen_ret=s.listen()
        print(f'listening on {host}:{port}')
        
        conn, remote_addr = s.accept()
        print(f'received connection from {remote_addr}')
        while(True):
            data=conn.recv(1024)
            if not data:
                continue #wait for more data
            decoded_msg=data.decode('utf-8').strip()
            print(f'received message from {remote_addr}: {decoded_msg}[{len(decoded_msg)}]')
            if decoded_msg=='exit':
                print(f'received exit message')
                conn.close()
                s.close()
                sys.exit(0)
            #echo the data
            conn.sendall(data)

if __name__ == '__main__':
    main()
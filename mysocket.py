#!bin/python3

#SOCKETS
import socket

host = 127.0.0.1
port = 7777

#AF_INET = ipv4 
#SOCK_STREAM = tcp port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.connect((host, port))

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((' ', 10458)) #ip 주소, 포트 넘기기

print("server 대기중")
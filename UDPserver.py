import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('localhost', 10458)) #ip 주소, 포트 넘기기

print("server 대기중")

while True:
    # read datagram from server socket
    data, client_address = server_socket.recvfrom(1024)
    print("Received : ", data.decode, " - ", client_address)
    
    # write reply to server socket specifying client address, port
    server_socket.sendto(data, client_address)
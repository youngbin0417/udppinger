import socket

def load_ip(filename): 
    with open(filename, 'r') as f:
        return f.read().strip()

server_ip = load_ip('config.txt')
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((server_ip, 10458)) #ip 주소, 포트 넘기기
print("server 바인딩 성공: ",server_ip,":10458")

print("server 대기중")

while True:
    # read datagram from server socket
    data, client_address = server_socket.recvfrom(1024)
    print("Received : ", data.decode(), " - ", client_address)
    
    # write reply to server socket specifying client address, port
    server_socket.sendto(data, client_address)
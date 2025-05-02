import socket

def load_ip(filename): 
    with open(filename, 'r') as f:
        return f.read().strip()

# ip주소가 들어간 config.txt를 로컬에 둠
server_ip = load_ip('config.txt')
server_port = 10458

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
    message = f"PING {i}"
    
    # create datagram with serverIP address
    client_socket.sendto(message.encode(), (server_ip, server_port))
    
    # read datagram
    data, _ = client_socket.recvfrom(1024)
    print("Response :", data.decode())
    
# close socket
client_socket.close()

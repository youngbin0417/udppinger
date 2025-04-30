import socket

server_ip = ''
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

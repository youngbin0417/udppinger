import socket
import time

def load_ip(filename): 
    with open(filename, 'r') as f:
        return f.read().strip()

# ip주소가 들어간 config.txt를 로컬에 둠
server_ip = load_ip('config.txt')
server_port = 10458

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)

rtts=[]
loss_count=0

for i in range(5):
    message = f"PING {i}"
    start_time=time.time()
    
    try:
        # create datagram with serverIP address
        client_socket.sendto(message.encode(), (server_ip, server_port))
        print(f"Sending to {server_ip}:{server_port} → {message}")

        # read datagram
        data, _ = client_socket.recvfrom(1024)
        end_time=time.time()
        
        rtt=(end_time-start_time) * 1000
        rtts.append(rtt)
        print(f"Response: {data.decode()} | RTT: {rtt:.2f} ms")
        
    except socket.timeout:
        print(f"Request {i} timed out.")
        loss_count += 1
        
    time.sleep(1)
    
# close socket
client_socket.close()

if rtts:
    print(f"Average RTT: {sum(rtts)/len(rtts):.2f} ms")
    print(f"Min RTT: {min(rtts):.2f} ms")
    print(f"Max RTT: {max(rtts):.2f} ms")
else:
    print("No response")

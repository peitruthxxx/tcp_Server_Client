import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello!!!')
    data = s.recv(1024)

print('Received',repr(data)) #讓python直接看懂'data' 若使用str會丟失data所含數據信息
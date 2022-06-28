import socket

HOST = '75.119.133.43'  # The server's hostname or IP address
ipconfig/s
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Salom olam')
    data = s.recv(1024)

    print('Received', repr(data))
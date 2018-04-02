import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"  # server address
port =9999  #server port
s.connect((host,port))
print(s.recv(1024))
s.send(b'Hello Server')
s.close()
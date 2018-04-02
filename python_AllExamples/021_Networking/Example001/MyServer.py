import socket
host = "localhost" #Server address
port = 9999  #Port of Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #bind server
s.listen(2)
conn, addr = s.accept()
print(addr, "Now Connected")
conn.send(b'Thank you for connecting')
conn.close()
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
while True;
clientsocket, address=s.accept()
print(f"connection from {address}has beeb established!")
clientsocket.send(bytes("welcome to the server!","ütf-8"))

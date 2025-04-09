import socket
Xa=3
a=6
q=11
Ya=((a)**Xa)%q
print(Ya)
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',12000)
clientSocket.sendto(str(Ya).encode(),addr)

#Recv Ya1 from hacker
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',12001))
Ya1,addr=serverSocket.recvfrom(1024)
Ya1=int(Ya1)

Kax=(Ya1)**Xa%q
print(Kax)


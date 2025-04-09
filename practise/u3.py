import socket
Xb=5
a=6
q=11
#Recv Yb1 from hacker
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',12002))
Yb1,addr=serverSocket.recvfrom(1024)
Yb1=int(Yb1)

#Send Yb to Hacker
Yb=(a**Xb)%q
print(Yb)
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',12003)
clientSocket.sendto(str(Yb).encode(),addr)

print("Kbx",(Yb1**Xb)%q)
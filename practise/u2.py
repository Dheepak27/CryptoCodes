import socket
Xa1=2
Xb1=4
a=6
q=11

#Recv Ya from A
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',12000))
Ya,addr=serverSocket.recvfrom(1024)
Ya=int(Ya)

#Send Ya1 to A
Ya1=((a)**Xa1)%q
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',12001)
clientSocket.sendto(str(Ya1).encode(),addr)

#Send Yb1 to B
Yb1=((a)**Xb1)%q
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',12002)
clientSocket.sendto(str(Yb1).encode(),addr)

#Recv Yb from B
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',12003))
Yb,addr=serverSocket.recvfrom(1024)
Yb=int(Yb)

print("Kax",Ya**Xa1%q)
print("Kbx",Yb**Xb1%q)
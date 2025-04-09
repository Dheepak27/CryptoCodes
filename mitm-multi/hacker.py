import socket
a=6
q=11


#Hacker select random key Xa1 to find Ya1
Xa1=2
Ya1=a**Xa1%q


#recv Ya from A pretending to be B
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 12000))
cipher, addr = serverSocket.recvfrom(1024)
Ya=int(cipher.decode())
print("Ya Received from A",Ya)



#send Ya1 to A
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1', 12001)
st=str(Ya1)
clientSocket.sendto(st.encode(), addr)
print("Ya1 Key by hacker for A",Ya1)


#Hacker select random key Xb1 to find Yb1
Xb1=4
Yb1=a**Xb1%q


#send Yb1 to B 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1', 12002)
st=str(Yb1)
clientSocket.sendto(st.encode(), addr)
print("Yb1 Key by hacker for B",Yb1)

#recv Yb from B pretending to be A
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 12003))
cipher, addr = serverSocket.recvfrom(1024)
Yb=int(cipher.decode())
print("Yb Received from B",Yb)

#cal Kax and Kbx
Kax=Ya**Xa1%q
Kbx=Yb**Xb1%q
print("Kax",Kax)
print("Kbx",Kbx)

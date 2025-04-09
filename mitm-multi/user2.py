import socket
a=6
q=11

#cal user2 public key
Xb=5
Yb=a**Xb%q

#recv Yb1 from A without knowing it is from hacker
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 12002))
cipher, addr = serverSocket.recvfrom(1024)
Yb1=int(cipher.decode())
print("Yb1 Received from A(hacker)",Yb1)

#Find key Kbx
Kbx=(Yb1)**Xb%q
print("Kbx",Kbx)

#send Yb to A but hacker hears it 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1', 12003)
st=str(Yb)
clientSocket.sendto(st.encode(), addr)
print("Yb",Yb)

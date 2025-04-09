import socket
q=11
a=6

#cal A public key
Xa=3
Ya=a**Xa%q
print("Ya",Ya)

#send Ya to B but hacker hears it 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1', 12000)
st=str(Ya)
clientSocket.sendto(st.encode(), addr)


#recv Ya1 without knowing it is from hacker
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 12001))
cipher, addr = serverSocket.recvfrom(1024)
Ya1=int(cipher.decode())
print("Ya1 from B(hacker)",Ya1)

#Find key Kax
Kax=Ya1**Xa%q
print("Kax",Kax)



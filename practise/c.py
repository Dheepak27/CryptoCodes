import socket

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',12000)
p=int(input('Enter p: '))
q=int(input('Enter q: '))
n=p*q
phin=(p-1)*(q-1)
e=int(input('Enter e: '))
M=int(input('Enter M: '))
C=(M**e)%n
print(C)
cipher=str(n)+" "+str(phin)+" "+str(e)+" "+str(C)
clientSocket.sendto(cipher.encode(),addr)
import socket


def modinv(e,phin):
    i=1
    while(True):
        if(e*i%phin==1):
            return i 
        i+=1

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',1200))
encr,addr=serverSocket.recvfrom(1024)
encr=encr.decode()
Xa=int(input('Enter Xa:'))
a=int(input("Enter a: "))
q=int(input("Enter q: "))
C1,C2=map(int,encr.split())
print(C1,C2)
K=((C1)**Xa)%q
inv=modinv(K,q)
M=(C2*inv)%q
print(M)

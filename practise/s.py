import socket



def modinv(e,phin):
    i=1
    while(True):
        if(e*i%phin==1):
            return i
        i+=1 
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',12000))
cipher,addr=serverSocket.recvfrom(1024)
cipher=cipher.decode()
n,phin,e,C=map(int,cipher.split())
d=modinv(e,phin)
M=(C**d)%n
print(M)

import socket


def invmod(n1,n2):
    i=0
    while(True):
        if((i*n1)%n2==1):
            return i 
        i+=1


while(True):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', 12000))
    cipher, addr = serverSocket.recvfrom(1024)
    CT=cipher.decode()
    CT=list(map(int,CT.split()))
    C1=CT[0]
    C2=CT[1]
    a=int(input('Enter a:'))
    q=int(input('Enter q:'))
    Xa=int(input('Enter Xa:'))
    print("Recived as (C1,C2):",C1,C2)
    Ya=a**Xa % q
    print("Ya:",Ya)
    K=(C1)**Xa%q
    t=invmod(K,q)
    M=(C2*t) % q
    print('Decrypted:',M)
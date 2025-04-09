import socket


def invmod(n1,n2):
    i=0
    while(True):
        if((i*n1)%n2==1):
            return i 
        i+=1



while True:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', 12000))
    cipher, addr = serverSocket.recvfrom(1024)
    l=list(map(int,(cipher.decode()).split()))
    if(l[0]==0):
        break
    elif(l[0]!=0):
        print("Recieved as c,e,phi(n),n")
        print(cipher.decode())
        d=invmod(l[1],l[2])
        print("Decrypted:",l[0]**d%l[3])

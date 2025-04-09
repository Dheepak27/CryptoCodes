import socket
import math

def decode(msg,key,n):
    k=1
    ind=0
    l=[]
    org=msg
    for i in range(math.ceil(len(msg)/n)):
        t=[]
        for j in range(n):
            t.append(' ')
        l.append(t)

    for i in range(n):
        col=key.index(str(k))
        for j in range(math.ceil(len(msg)/n)):
            l[j][col]=msg[ind]
            ind+=1
        k+=1
    print("Matrix: ")
    msg=""
    for i in range(math.ceil(len(org)/n)):
        for j in range(n):
            print(l[i][j],end=' ')
            msg+=l[i][j]
        print()
    return msg

        


while True:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', 12400))
    cipher, addr = serverSocket.recvfrom(1024)
    encrypted=cipher.decode()
    n=int(input("Enter n: "))
    key=input("Enter Key: ")
    print("Cipher Text:",encrypted)
    decrypted=decode(encrypted,key,n)
    print("Decrypted Text:",decrypted)
    if decrypted=="EXITEXITEXITEXIT":
        break
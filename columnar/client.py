import socket
import math
def makemat(msg,n):
    l=[]
    t=[]
    for i in range(0,len(msg)):
        t.append(msg[i])
        if(len(t)==n):
            l.append(t)
            t=[]
    print(t)
    if(len(t)>0):
        while(len(t)<n):
            t.append(' ')
    l.append(t)
    return l

def encrypt(l,key,org):
    msg=""
    k=1
    for i in range(math.ceil(len(org)/n)):
        col=-1
        for j in range(n):
            if key[j]==str(k):
                col=j
            if(col!=-1):
                for p in range(math.ceil(len(org)/n)):
                    msg+=l[p][col]
                break
        k+=1
    return msg 

while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12400)
    n=int(input("Enter n: "))
    key=input("Enter Key: ")
    msg=input("Enter Message: ")
    l=makemat(msg,n)
    print("Matrix: ")
    for i in range(math.ceil(len(msg)/n)):
        for j in range(n):
            print(l[i][j] ,end=" ")
        print()
    encrypted=encrypt(l,key,msg)
    print(encrypted)
    clientSocket.sendto(encrypted.encode(), addr)
    if msg=="EXITEXITEXITEXIT":
        break
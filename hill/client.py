import socket

def getmsgmatrix(msg):
    mat=[]
    for i in range(0,len(msg)):
        mat.append(ord(msg[i])-65)
    print(mat)
    return mat

def encyrpt(keymat,msgmat):
    ans=""
    for i in range(0,len(keymat)):
        sum=0
        for j in range(0,len(keymat)):
            sum+=keymat[i][j]*msgmat[j]
        ans+=chr(sum%26+65)
    return ans

while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12400)
    n=int(input())
    print('Enter Key Matrix: ')
    keymat=[]
    for i in range(n):
        l=[]
        for j in range(n):
            x=int(input())
            l.append(x)
        keymat.append(l)
    print(keymat)
    msg=input("Enter Message: ")
    msgmat=getmsgmatrix(msg)
    encyrpted=encyrpt(keymat,msgmat)
    print(encyrpted)
    clientSocket.sendto(encyrpted.encode(), addr)
    if msg=="BYE":
        break










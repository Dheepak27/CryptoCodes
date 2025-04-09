import socket

def createfence(depth,msg):
    n=len(msg)
    l=[]
    for i in range(depth):
        t=[]
        for j in range(n):
            t.append(' ')
        l.append(t)
    ind=0
    i=0
    j=0
    while(True):
        while(i<depth):
            if(ind>=len(msg)):
                break
            l[i][j]=msg[ind]
            i+=1
            j+=1
            ind+=1
        i-=2
        while(i>=0):
            if(ind>=len(msg)):
                break
            l[i][j]=msg[ind]
            i-=1
            j+=1
            ind+=1
        i+=2
        if(ind>=len(msg)):
            break
    msg=""
    for i in range(depth):
        for j in range(n):
            print(l[i][j],end=" ")
            if(l[i][j]!=" "):
                msg+=l[i][j]
        print()
    return msg





while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12400)
    depth=int(input("Enter Depth: "))
    msg=input("Enter Message: ")
    encrypted=createfence(depth,msg)
    print("Encrypted Text:",encrypted)
    clientSocket.sendto(encrypted.encode(), addr)
    if msg=="EXIT":
        break




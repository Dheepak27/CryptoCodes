import socket

def decodefence(msg,depth):
    #create list
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
    #mark places where character comes
    while(True):
        while(i<depth):
            if(ind==len(msg)):
                break
            l[i][j]='.'
            i+=1
            j+=1
            ind+=1
        i-=2
        while(i>=0):
            if(ind==len(msg)):
                break
            l[i][j]='.'
            i-=1
            j+=1
            ind+=1
        i+=2
        if(ind==len(msg)):
            break
    #place the characters in cipher text in the fence
    ind=0
    for i in range(depth):
        for j in range(n):
            if(l[i][j]=='.' and ind<len(msg)):
                l[i][j]=msg[ind]
                ind+=1
    for i in range(depth):
        for j in range(n):
            print(l[i][j],end=" ")
        print()
    #obtaining result by re-traversing
    ans=""
    i=0
    j=0
    ind=0
    while(True):
        while(i<depth):
            if(ind==len(msg)):
                break
            ans+=l[i][j]
            i+=1
            j+=1
            ind+=1
        i-=2
        while(i>=0):
            if(ind==len(msg)):
                break
            ans+=l[i][j]
            i-=1
            j+=1
            ind+=1
        i+=2
        if(ind==len(msg)):
            break   
    return ans


while True:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', 12400))
    cipher, addr = serverSocket.recvfrom(1024)
    encrypted=cipher.decode()
    depth=int(input("Enter Depth: "))
    print("Cipher Text:",encrypted)
    decrypted=decodefence(encrypted,depth)
    print("Decypted Text:",decrypted)
    if decrypted=="EXIT":
        break
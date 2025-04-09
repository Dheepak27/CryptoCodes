import socket

def encrypt(msg,table):
    encrypted=""
    for i in range(0,len(msg),2):
        sub=msg[i:i+2]

        row1=-1
        col1=-1
        row2=-1
        col2=-1

        for j in range(0,5):
            for k in range(0,5):
                if(table[j][k]==sub[0]):
                    row1=j
                    col1=k 
                    break
            if(row1!=-1 and col1!=-1):
                break 
        
        for j in range(0,5):
            for k in range(0,5):
                if(table[j][k]==sub[1]):
                    row2=j
                    col2=k 
                    break
            if(row2!=-1 and col2!=-1):
                break 
        if(col1==col2):
            encrypted+=table[(row1+1)%5][col1]+table[(row2+1)%5][col2]
        elif(row1==row2):
            encrypted+=table[row1][(col1+1)%5]+table[row2][(col2+1)%5]
        else:
            encrypted+=table[row1][col2]+table[row2][col1]
    print(encrypted)
    return encrypted

                

        

def gettable(msg):
    unq=[];l=[];temp=[];k=0
    for i in msg:
        if i not in unq:
            unq.append(i)
    for i in range(5):
        t=[]
        for j in range(5):
            t.append(' ')
        l.append(t)
    for i in unq:
        temp.append(i)
    for j in range(97,123):
        c=chr(j)
        if c not in temp:
            temp.append(c)
    for i in range(0,5):
        for j in range(0,5):
            if(temp[k]=='j'):
                k+=1
            l[i][j]=temp[k]
            k+=1
    for i in range(5):
        for j in range(5):
            print(l[i][j],end=" ")
        print()
    return l
    


def changetext(msg):
    ans=""
    for i in range(0,len(msg)-1):
        if msg[i]==msg[i+1]:
            ans+=msg[i]+'x'
        else:
            ans+=msg[i]
    ans+=msg[len(msg)-1]
    if(len(ans)%2!=0):
        ans+='x'
    print(ans)
    return ans

while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12000)
    msg=input("Enter Message: ")
    key=input("Enter Key: ")
    msg=msg.lower()
    msg=msg.replace(" ","")
    changed=changetext(msg)
    table=gettable(key)
    encrypted=encrypt(changed,table)
    clientSocket.sendto(encrypted.encode(), addr)
    if(msg=="exit"):
        break










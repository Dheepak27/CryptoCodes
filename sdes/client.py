import socket
def lcs(num,d):
    left=num[:d]
    right=num[d:]
    return (right+left)


def calp10(k):
    p10=[3,5,2,7,4,10,1,9,8,6]
    p10st=""
    for i in range(0,len(p10)):
        p10st+=k[p10[i]-1]
    return p10st

def calkey(p10st):
    lp10=p10st[:5]
    rp10=p10st[5:]
    lp10r=lcs(lp10,1)
    rp10r=lcs(rp10,1)
    sh1=lp10r+rp10r
    p8=[6,3,7,4,8,5,10,9]
    sk1=""
    for i in range(len(p8)):
        sk1+=sh1[p8[i]-1]
    lp10rr=lcs(lp10r,2)
    rp10rr=lcs(rp10r,2)
    sh2=lp10rr+rp10rr
    sk2=""
    for i in range(len(p8)):
        sk2+=sh2[p8[i]-1]
    return sk1,sk2


def calinitalperm(pt):
    ip=[2,6,3,1,4,8,5,7]
    ptip=""
    for i in range(0,len(ip)):
        ptip+=pt[ip[i]-1]
    return ptip

def complexfuncenc(ptip,sk1,sk2):
    #complex function with sk1
    #exponential permutation
    ep=[4,1,2,3,2,3,4,1]
    s0box=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1box=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    p4=[2,4,3,1]
    ip=[4,1,3,5,7,2,8,6]
    l=ptip[:4]
    r=ptip[4:]
    expperm=""
    for i in range(0,len(ep)):
        expperm+=r[ep[i]-1]
    print("Exponential Permutation: ",expperm)
    #xor
    xor=""
    for i in range(len(expperm)):
        if(expperm[i]==sk1[i]):
            xor+="0"
        else:
            xor+="1"
    print("XOR: ",xor)
    #substitution
    s0r=xor[0]+xor[3]
    s0c=xor[1:3]
    s1r=xor[4]+xor[7]
    s1c=xor[5:7]
    print("Rows and Columns: ")
    print(s0r,s0c,s1r,s1c)
    s0=s0box[int(s0r,2)][int(s0c,2)]
    s1=s1box[int(s1r,2)][int(s1c,2)]
    print(s0,s1)
    s0s1=""
    if(len(bin(s0)[2:])!=2):
        s0s1+="0"
    s0s1+=bin(s0)[2:]
    if(len(bin(s1)[2:])!=2):
        s0s1+="0"
    s0s1+=bin(s1)[2:]
    print("Concat: ",s0s1)
    #permutation p4
    p4st=""
    for i in range(len(p4)):
        p4st+=s0s1[p4[i]-1]
    print("P4: ",p4st)
    #final
    final1=""
    for i in range(len(p4)):
        if(p4st[i]==l[i]):
            final1+="0"
        else:
            final1+="1"
    final1+=r 
    print("L^F(R,SK1)R: ",final1)
    #swap
    swapped=final1[4:]+final1[:4]
    print("Swap: ",swapped)
    #complex function with sk2
    #exponential permutation
    l=swapped[:4]
    r=swapped[4:]
    expperm=""
    for i in range(0,len(ep)):
        expperm+=r[ep[i]-1]
    print("Exponential Permutation:",expperm)
    #xor
    xor=""
    for i in range(len(expperm)):
        if(expperm[i]==sk2[i]):
            xor+="0"
        else:
            xor+="1"
    print("XOR: ",xor)
    #substitution
    s0r=xor[0]+xor[3]
    s0c=xor[1:3]
    s1r=xor[4]+xor[7]
    s1c=xor[5:7]
    print("Rows and Columns: ")
    print(s0r,s0c,s1r,s1c)
    s0=s0box[int(s0r,2)][int(s0c,2)]
    s1=s1box[int(s1r,2)][int(s1c,2)]
    print(s0,s1)
    s0s1=""
    if(len(bin(s0)[2:])!=2):
        s0s1+="0"
    s0s1+=bin(s0)[2:]
    if(len(bin(s1)[2:])!=2):
        s0s1+="0"
    s0s1+=bin(s1)[2:]
    print("Concat: ",s0s1)
    #permutation p4
    p4st=""
    for i in range(len(p4)):
        p4st+=s0s1[p4[i]-1]
    print("P4: ",p4st)
    #final
    temp=""
    for i in range(len(p4)):
        if(p4st[i]==l[i]):
            temp+="0"
        else:
            temp+="1"
    temp+=r 
    print("L^F(R,SK2)R: ",temp)
    #apply inverseperm
    ciphertext=""
    for i in range(len(ip)):
        ciphertext+=temp[ip[i]-1]
    return ciphertext


while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12000)
    k=input("Enter K: ")
    p10st=calp10(k)
    print("P10: ",p10st)
    sk1,sk2=calkey(p10st)
    print("SK1,SK2: ",sk1,sk2)
    pt=input("Enter Plain-Text: ")
    ptip=calinitalperm(pt)
    print("Initial Permutation: ",ptip)
    encrypted=complexfuncenc(ptip,sk1,sk2)
    print("Cipher Text: ",encrypted)
    clientSocket.sendto(encrypted.encode(), addr)
    if pt=="00000000":
        break
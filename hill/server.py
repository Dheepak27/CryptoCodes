import socket
import numpy as np
from sympy import mod_inverse

def calinv(keymat):
    A = np.array(keymat)
    det = round(np.linalg.det(A))
    det_mod = det % 26
    try:
        det_inv = mod_inverse(det_mod, 26)
    except ValueError:
        raise ValueError("Determinant has no modular inverse under mod 26.")
    adjugate = np.round(det * np.linalg.inv(A)).astype(int) % 26
    inverse_matrix = (det_inv * adjugate) % 26
    return inverse_matrix.astype(int)

def getencmatrix(msg):
    mat=[]
    for i in range(0,len(msg)):
        mat.append(ord(msg[i])-65)
    return mat

def getmsg(invkeymat,encmat):
    ans=""
    for i in range(0,len(invkeymat)):
        sum=0
        for j in range(0,len(invkeymat)):
            sum+=invkeymat[i][j]*encmat[j]
        ans+=chr(sum%26+65)
    return ans

while True:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', 12400))
    cipher, addr = serverSocket.recvfrom(1024)
    encrypted=cipher.decode()
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
    print("Inverse Key Matrix: ")
    invkeymat=calinv(keymat)
    print(np.array(invkeymat).tolist())
    encmat=getencmatrix(encrypted)
    print("Encrypted text Matrix: ")
    print(encmat)
    text=getmsg(invkeymat,encmat)
    print(text)
    if text=="BYE":
        break
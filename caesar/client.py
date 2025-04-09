import socket

def encrypt(msg,key):
    encrypted=""
    j=0
    for i in range(0,len(msg)):
        if j>3:
            j=0
        k=int(key[j])
        val=ord(msg[i])
        if msg[i].isupper():
            val=(((ord(msg[i])-65)+k)%26)+65
        elif msg[i].islower():
            val=(((ord(msg[i])-97)+k)%26)+97
        encrypted+=chr(val)
        j+=1
    return encrypted

while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12000)
    msg=input("Enter Message: ")
    key=input("Enter Key: ")
    encrypted=encrypt(msg,key)
    print(encrypted)
    clientSocket.sendto(encrypted.encode(), addr)
    if msg=="exit":
        break










import socket

def decrypt(msg,key):
    encrypted=""
    j=0
    for i in range(0,len(msg)):
        if j>3:
            j=0
        k=int(key[j])
        val=ord(msg[i])
        if msg[i].isupper():
            val=(((ord(msg[i])-65)-k)%26)+65
        elif msg[i].islower():
            val=(((ord(msg[i])-97)-k)%26)+97
        encrypted+=chr(val)
        j+=1
    return encrypted

while True:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', 12000))
    key=input("Enter Key: ")
    cipher, addr = serverSocket.recvfrom(1024)
    encrypted=cipher.decode()
    print(encrypted)
    decoded=decrypt(encrypted,key)
    print(decoded)
    if decoded=="exit":
        break
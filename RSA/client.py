import socket



while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12000)
    p=int(input("Enter p: "))
    q=int(input("Enter q: "))
    n=p*q
    phin=(p-1)*(q-1)
    e=int(input("Enter e: "))
    M=int(input("Enter M: "))
    c=0
    if(n!=0):
        c=(M**e)%n
    st=str(c)+" "+str(e)+" "+str(phin)+" "+str(n)
    clientSocket.sendto(st.encode(), addr)
    if n==0:
        break

import socket



while(True):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr=('127.0.0.1', 12000)
    q=int(input('Enter q:'))
    a=int(input('Enter a:'))
    Ya=int(input('Enter Ya:'))
    M=int(input('Enter M:'))
    k=int(input('Enter k:'))

    K=(Ya)**k % q
    print('K:',K)
    C1=(a)**k % q 
    C2=K*M % q
    CT=str(C1)+" "+str(C2)
    print(C1,C2)
    clientSocket.sendto(CT.encode(), addr)





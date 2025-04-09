import socket



a=int(input("Enter a: "))
q=int(input("Enter q: "))
k=int(input("Enter k: "))
Ya=int(input("Enter Ya: "))
M=int(input("Enter M: "))
K=Ya**k
C1=(a**k)%q
C2=(K*M)%q 
C=str(C1)+" "+str(C2)
print(C)
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',12005)
clientSocket.sendto(C.encode(),addr)
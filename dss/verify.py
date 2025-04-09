import socket

def modinv(x,y):
    i=1
    while(True):
        if((x*i)%y==1):
            return i
        i+=1




serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 12400))
p=int(input('Enter p: '))
q=int(input('Enter q: '))
signature, addr = serverSocket.recvfrom(1024)
signature=signature.decode()
r,s,Hm,g,y=map(int,signature.split())
print("Received r,s,Hm,g,y: ",r,s,Hm,g,y)
#verifying
w=modinv(s,q)
v1=(Hm*w)%q
v2=(r*w)%q
print("V1:",v1)
print("V2:",v2)
v=(((g**v1)*(y**v2))%p)%q
print("V:",v)
if(v==r):
    print("Verified")
else:
    print("Not Verified")
import socket
def modinv(x,y):
    i=1
    while(True):
        if((x*i)%y==1):
            return i
        i+=1





clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1', 12400)
p=int(input('Enter p: '))
q=int(input('Enter q: '))
h=int(input('Enter h: '))
g=(h**((p-1)//q))%p
print('g:',g)
x=int(input('Enter x: '))
y=(g**x)%p
print('y:',y)
Hm=int(input('Enter H(m): '))
k=int(input('Enter k: '))
#signing 
r=((g**k)%p)%q
inv=modinv(k,q)
s=inv*(Hm+x*r)%q
print("Signature (r,s):",r,s)
send=str(r)+" "+str(s)+" "+str(Hm)+" "+str(g)+" "+str(y)
clientSocket.sendto(send.encode(), addr)

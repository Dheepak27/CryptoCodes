import hashlib


k=input("Enter Key ")
ipad="00110110"
opad="01011100"

c=len(k)//8
if(len(k)//8!=0):
    c+=1
if(len(k)>8):
    ipad=ipad*c
    opad=opad*c

k=int(k,2)
ipad=int(ipad,2)
opad=int(opad,2)
print("K - ",k)
print("Ipad - ",ipad)
print("Opad - ",opad)

msg1=input("Enter message ") 
msg1=msg1.encode('ascii')
temp=str(k^ipad).encode('ascii')
msg1=temp+msg1
print("Message 1 - ",msg1)
hash1=hashlib.sha512(msg1)
hash1=hash1.hexdigest().encode()
print("H( (K' ^ ipad) || m) - ",hash1)




msg2=str(k^opad).encode('ascii')+hash1
print("Message 2 - ",msg2)
hash2=hashlib.sha512(msg2)
hash2=hash2.hexdigest().encode()
print("H( (K' ^ opad) || H( (K' ^ ipad) || m))) - ",hash2)


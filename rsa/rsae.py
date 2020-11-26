import time
import sys
def gcd(a,b):
    while a!=b:
        if(a>b):
            a-=b
        else:
            b-=a
    return a
def e(p):
    for i in range(2,p):
        if(gcd(i,p)==1):
            break
    return i
        
def n(a,b):
    return a*b
def phi(a,b):
    return (a-1)*(b-1)
def d(p,e):
    r1=p
    r2=e
    t1=0
    t2=1
    r=r1%r2
    q=r1//r2
    t=t1-q*t2
    print("\t\tp\t\tr1\t\tr2\t\tr\t\tt1\t\tt2\t\tt")
    print("\t\t"+str(q)+"\t\t"+str(r1)+"\t\t"+str(r2)+"\t\t"+str(r)+"\t\t"+str(t1)+"\t\t"+str(t2)+"\t\t"+str(t))
    while True:
        r1=r2
        r2=r
        t1=t2
        t2=t
        if(r2==0):
            break
        r=r1%r2
        q=r1//r2
        t=t1-q*t2
        print("\t\t"+str(q)+"\t\t"+str(r1)+"\t\t"+str(r2)+"\t\t"+str(r)+"\t\t"+str(t1)+"\t\t"+str(t2)+"\t\t"+str(t))   
    print("\t\t"+"\t\t"+str(r1)+"\t\t"+str(r2)+"\t\t"+"\t\t"+str(t1)+"\t\t"+str(t2)+"\t\t")
    print("Private Key: ")
    if(t1<0):
        print( p+t1)
    else:
        print(t1)
def encrypto(m,e,n):
    return pow(m,e)%n

M=sys.argv[1]
p=sys.argv[2]
q=sys.argv[3]
print("\t\t\t\t\t\t\t\t\tRSA Encryption\t\t\t\t\t\t\t\t\t")
print("Plaintext: " + M)
a=n(int(p),int(q))
print("n=pq="+str(p)+"*"+str(q)+"="+str(a))
b=phi(int(p),int(q))
print("(n)=(p-1)*(q-1)="+"("+str(p)+"-1)*("+str(q)+"-1)="+str(b))
c=e(b)
print("public key: "+str(c))
d(b,c)
e=encrypto(int(M),c,a)
print("Plain encrypt: " + str(e))

            
    


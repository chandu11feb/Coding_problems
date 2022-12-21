a=input().split()
n=a[0]
m=int(a[1])
price=[]
nutrition=[]
for _ in range(m):
    p,nu=input().split()
    price.append(p)
    nutrition.append(nu)
p=[]
b=[]
co=[]
fin=[]
import itertools
for i in range(1,len(price)+1):
    l=set(itertools.combinations(price,i))
    k=list(l)
    p=p+k
for j in p:
    bp=7
    pr=1
    for k in range(len(j)):
        h=j[k]
        pr=pr*int(h)
        ind=price.index(h)
        bina=int(nutrition[ind],2)
        bp= bp & bina
    b.append(bp)
    co.append(pr)
print(p)
print(co)
print(b)
ma=max(b)
for u in range(ma+1):
    #print(u)
    ki=0
    for r in range(len(b)):
        if b[r]==u:
            ki=ki+co[r]
            #print(co[r])
    if ki!=0:
        fin.append(ki)
for i in fin:
    print(i,end=" ")
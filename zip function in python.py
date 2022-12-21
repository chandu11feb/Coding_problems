n=int(input())
l=[]
s=[]
for i in range(n):
    a=input().split()
    nm=a[0]
    x=int(a[1])
    y=int(a[2])
    su=x+y
    l.append(nm)
    s.append(su)
w=tuple(l)
q=tuple(s)
z=zip(w,q)

print(tuple(z))
    
    
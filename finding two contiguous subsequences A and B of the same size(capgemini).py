n=int(input())
l=list(input().split())
a="".join(l)
prl=[]
size=1
def pro(f,s):
    f=str(f)
    s=str(s)
    s=list(s)
    s.reverse()
    s="".join(s)
    pr=0
    for i in range(len(f)):
        x=int(f[i])
        y=int(s[i])
        pr=pr+(x*y)
    return pr
while size<=len(a)//2:
    nl=[]
    for i in range(len(a)):
        if i+size <=len(a):
            x=int(a[i:i+size])
            nl.append(x)
    #print(nl)
    for i in range(len(nl)):
        for j in range(i+size+1,len(nl)):
            if len(str(nl[i]))==len(str(nl[j])):
                temp=pro(nl[i],nl[j])
                prl.append(temp)

    size+=1
print(max(prl))
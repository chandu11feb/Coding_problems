a=input()
b=a.split(" ")
c=[]
for i in range(len(b)):
    x=b.count(b[i])
    c.append(x)
print(c)
mi=min(c)
ma=max(c)
l=0
while mi<=ma:
    if(c[l]==mi):
        print(b[l],end=" ")
    l=l+1
    if l==len(b):
        l=0
        mi=mi+1
    
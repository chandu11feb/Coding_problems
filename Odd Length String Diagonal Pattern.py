a=input()
f=0
l=len(a)-1
while f<=l:
    for i in range(len(a)):
        if i==f or i==l:
            print(a[i],end="")
        else:
            print(" ",end="")
    print("\r")
    f=f+1
    l=l-1
n=int(len(a)/2)
f1=n-1
f2=n+1
while f1>=0 and f2<=len(a):
    for i in range(len(a)):
        if i==f1 or i==f2:
            print(a[i],end="")
        else:
            print(" ",end="")
    print("\r")
    f1=f1-1
    f2=f2+1
# subset sum problem (dynamic programming)
def ss(A,B):
    n=len(A)
    
    l=([[None for i in range(B+1)]
       for i in range(n+1)])
     
    for i in range(n+1):
        l[i][0]=True
    for j in range(B+1):
        l[0][j]=False
    
    for i in range(1,n+1):
        for j in range(1,B+1):
            if j-A[i-1] <0:
                l[i][j]=l[i-1][j]
            else:
                l[i][j]=l[i-1][j] or l[i-1][j-A[i-1]]
    if l[n][B]:
        m=n
        b=B
        s=set()
        while b>0:
            if l[m-1][b]:
                m=m-1
            else:
                m=m-1
                s.add(A[m])
                b=b-A[m]
        print(s)
    print(l)
    return l[n][B]
A=[10,20,30]
B=30
x=ss(A,B)
print(x)
        
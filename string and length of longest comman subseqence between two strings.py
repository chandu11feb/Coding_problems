# length and string of longest comman subsequence between two strings
def lcs(s1,s2):
    n,m=len(s1),len(s2)
    l=[[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if s1[i]==s2[j]:
                l[i+1][j+1]=l[i][j]+1
            else:
                l[i+1][j+1]=max(l[i+1][j],l[i][j+1])
    
    length=l[-1][-1]
    
    lc=[""]*(length+1)
    lc[length]=""
    i=n
    j=m
    
    while i>0 and j>0:
        if  s1[i-1]==s2[j-1]:
            lc[length-1]=s1[i-1]
            i-=1
            j-=1
            length-=1
        elif l[i-1][j] >l[i][j-1]:
            i-=1
        else:
            j-=1
    return "".join(lc),l[-1][-1]
s1='abcde'
s2='ace'
print(lcs(s1,s2))

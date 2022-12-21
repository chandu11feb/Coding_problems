# length of longest comman subsequence between two strings
def lcs(s1,s2):
    n,m=len(s1),len(s2)
    l=[[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if s1[i]==s2[j]:
                l[i+1][j+1]=l[i][j]+1
            else:
                l[i+1][j+1]=max(l[i+1][j],l[i][j+1])
    
    return l[-1][-1]
s1='abcde'
s2='ace'
print(lcs(s1,s2))
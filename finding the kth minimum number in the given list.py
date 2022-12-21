#finding the kth minimum number in the given list
l=[12,18,98,56,301,77,34,49,61]
k=5
m=max(l)
memo=[0]*(m+1)
for i in l:
    memo[i]=1
c=0
for i in range(m+1):
    if memo[i]==1:
        c+=1
        if c==k:
            print(i)
            break
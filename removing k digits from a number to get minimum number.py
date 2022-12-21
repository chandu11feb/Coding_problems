s="1432219"
k=3
r=len(s)-k
result=""
def fun(s,k,r):
    #print(r)
        
    if r==len(s):
        if s is not None:
            print(s)
            return s
    elif r==1:
        cv=min(list(s))
        return cv
    else:
        tem=s[:-(r-1)]
        print("r",r)
        print("tem"+tem)
        mi=min(list(tem))
        ind=s.index(mi)
        
        s=s[ind+1:]
        if r>1:
            print(mi)
            return mi+fun(s,k,r-1)
        else:
            print(mi)
            return mi
        print("str"+s)
result+=fun(s,k,r)
print(result)
        
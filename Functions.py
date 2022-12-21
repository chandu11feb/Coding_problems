

def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
            break
    if c==0:
        return 1
    else:
        return 0

def fact(n):
    fac=1
    while n>0:
        fac=fac*n
        n-=1
    return fac

# factorial of a number n using dynamic programming
result=[0]*1000
def fact(n):
    if n>0:
        result[0]=1
        for i in range(1,n+1):
            result[i]=i*result[i-1]
    return result[n]
print(fact(5))



def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)




def nprimes(n):
    l=[]
    for i in range(2,n):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                l.append(i)
    return l

def primecount(n):
    cont=0
    for i in range(2,n):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                cont+=1
    return cont

    

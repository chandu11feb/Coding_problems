s=[1,2,3,4,5]
p=[]
#n=scipy.misc.comb(s,m)
import itertools
for i in range(1,len(s)+1):
    l=set(itertools.combinations(s,i))
    k=list(l)
    p=p+k
    #print(p)
p.sort()
print(p)

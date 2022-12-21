n=5
a=[1,2,4,4,4,6,6,5,5,3,3,3]
import collections
l=dict(collections.Counter(a))
j=sorted(l.items(),key=lambda x:x[1])
print(j)
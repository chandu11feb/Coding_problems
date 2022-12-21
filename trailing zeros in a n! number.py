# trailing zeros in a n! number
s=0
n=15
x=n//5
while x>5:
    s+=x
    x=x//5
s+=x
print(s)
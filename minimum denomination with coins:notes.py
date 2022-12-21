coins=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
coins.sort()
amount=899322
n=len(coins)
result=False
def func(arr,am):
    count=0
    for i in arr[::-1]:
        if am==0:
            return am,count
        if am>=i:
            d=am//i
            am=am-(i*d)
            count+=d
            print(d,i,d*i)
    return am,count

while 1:
    if coins:
        am,cou=func(coins,amount)
        n=n-1
        coins=coins[:n]
        if am==0:
            print(cou)
            break
    else:
        print(-1)
        break

    
        
    
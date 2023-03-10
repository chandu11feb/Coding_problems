#Count ways to reach the nth stair using step 1, 2 or 3
def countWays(n) :
    res = [0] * (n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2
     
    for i in range(3, n + 1) :
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
    print(res)
    return res[n]

n = 5
print(countWays(n))
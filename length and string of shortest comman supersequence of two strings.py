def printShortestSuperSeq(x, y): 
    m = len(x) 
    n = len(y) 
  
    dp = [[0 for i in range(n + 1)]  
             for j in range(m + 1)] 
  
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            if i == 0: 
                dp[i][j] = j 
            elif j == 0: 
                dp[i][j] = i 
            elif x[i - 1] == y[j - 1]: 
                dp[i][j] = 1 + dp[i - 1][j - 1] 
            else: 
                dp[i][j] = 1 + min(dp[i - 1][j],  
                                   dp[i][j - 1]) 
  
    index = dp[m][n] 
    
    string = "" 
  
    
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        
        if x[i - 1] == y[j - 1]: 
  
            string += x[i - 1] 
  
            i -= 1
            j -= 1
            index -= 1
  
        elif dp[i - 1][j] > dp[i][j - 1]: 
  
            string += y[j - 1] 
  
            j -= 1
            index -= 1
        else: 
  
            string += x[i - 1] 
  
            i -= 1
            index -= 1
        
    while i > 0: 
        string += x[i - 1] 
        i -= 1
        index -= 1
  
    while j > 0: 
        string += y[j - 1] 
        j -= 1
        index -= 1
  
    string = list(string) 
    string.reverse() 
    
    return ''.join(string) , dp[m][n]
  
x = "AGGTAB"
y = "GXTXAYB"
  
print(printShortestSuperSeq(x, y))
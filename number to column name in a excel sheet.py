#number to column name in a excel sheet
# 1 A 2 B .....27 AA 28 AB...
def col(num):
    r=""
    while num>0:
        i=(num-1)%26
        r+=chr(i+ord('A'))
        num=(num-1)//26
    return r[::-1]
print(col(1))
def findOppositeNumber(n,m): 
    if m > (n/2):
        return int(m-(n/2))
    elif m == n/2 : 
        return 0 
    else : 
        return int(m + (n/2))
print(findOppositeNumber(10,6))
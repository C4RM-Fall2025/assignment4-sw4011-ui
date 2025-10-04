def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    cf = face * couponRate / ppy
    pv = 0
    for i in range (1,n+1):
        pv = pv + cf / (1 + r) ** i
    
    pvsum= pv + face / (1 + r) ** n
    return(pvsum)

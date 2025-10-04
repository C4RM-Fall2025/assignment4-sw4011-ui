def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = m * ppy
    r = y / ppy
    cf = face * couponRate / ppy
    
    pvcfSum = 0
    pvcfTime = 0
    
    for i in range(1,n+1):
        if i < n:
            cashflow = cf
        else:
            cashflow = cf + face
            
        discount = 1 / (1 + r) ** i
        pvcfSum = pvcfSum + cashflow * discount
        pvcfTime = pvcfTime + i * cashflow * discount

    getBondDuration = pvcfTime / pvcfSum / ppy
    return(getBondDuration)

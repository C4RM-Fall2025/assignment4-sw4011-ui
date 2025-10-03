def getBondPrice_E(face, couponRate, m, yc):
    cf = face * couponRate 
    pv = 0
    
    for i in range(1, m+1):
        cashflow = cf
        if i == m:
            cashflow += face
        discount_factor = 1 / (1 + yc[i-1])**i
        
        pv += cashflow * discount_factor
    
    return pv

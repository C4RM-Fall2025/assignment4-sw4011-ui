def getBondPrice_E(face, couponRate, m, yc):
    assert len(yc) == m
    cf = face * couponRate
    pv = 0

    for i in range(1, m+1):
        if i < m:
            cashflow = cf
        else:
            cashflow = cf + face

        discount = 1
        for k in range(i):
            discount = (1 + yc[k]) ** i
        discount = 1 / discount

        pv += cashflow * discount
    
    return pv

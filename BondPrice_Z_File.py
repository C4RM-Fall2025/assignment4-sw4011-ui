def getBondPrice_Z(face, couponRate,times, yc):
    cf = face * couponRate 
    pv = 0
    for t,y in zip(times,yc):
        if t == max(times):
            pv += (face + cf) / (1 + y) ** t
        else :
            pv += cf / (1 + y) ** t
    return(pv)

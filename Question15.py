def rectangles_overlap(L1, R1, L2, R2):
    x1, y1 = L1
    x2, y2 = R1
    x3, y3 = L2
    x4, y4 = R2
    
    # if one rectangle is to left of other
    if x2 < x3 or x4 < x1:
        return False
    # if one rectangle is above other
    if y2 > y3 or y4 > y1:
        return False
    
    return True
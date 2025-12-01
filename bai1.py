def BCNN(a, b):
    if a > b:
        return BCNN(a - b, b)
    if a < b:
        return BCNN(a, b - a)
    return b


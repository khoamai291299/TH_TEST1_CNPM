def ktra3canhtamgiac(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return 1
    return 0

def ktratamgiac(a, b, c):
    if ktra3canhtamgiac(a, b, c) == 1:
        if (a == b) or (a == c) or (b == c):
            if a == b == c:
                return 1
            else:
                return 2
        else:
            if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
                return 3
    else:
        return 0
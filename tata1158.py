def sa(a):
    if len(a) >= 2:
        x = a[0]
        a[0] = a[1]
        a[1] = x
    return a


def sb(b):
    if len(b) >= 2:
        x = b[0]
        b[0] = b[1]
        b[1] = x
    return b

def ss(a, b):
    a = sa(a)
    b = sb(b)
    return a, b

def pa(a, b):
    if len(b) == 0:
        return a, b
    x = b.pop(0)
    a.insert(0, x)
    return a, b

def pb(a, b):
    if len(a) == 0:
        return a, b
    x = a.pop(0)
    b.insert(0, x)
    return a, b

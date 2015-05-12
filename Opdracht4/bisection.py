def findRoot(f,a,b,epsilon):
    m = (a + b)/2
    if abs(b - a) <= epsilon or f(m) == 0:
        return m
    elif f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    elif f(b) > 0:
        if f(m) > 0:
            return findRoot(f,a,m,epsilon)
        else:
            return findRoot(f,m,b,epsilon)
    elif f(b) < 0:
        if f(m) < 0:
            return findRoot(f,a,m,epsilon)
        else:
            return findRoot(f,m,b,epsilon)    
    else:
        return 'Error!'
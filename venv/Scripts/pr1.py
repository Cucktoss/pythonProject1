def f(x,y):
    t = 0
    while(x>0):
        if(x%2==1):
            t+=y
        x //= 2
        y *= 2
    return t
print(f(14,11))

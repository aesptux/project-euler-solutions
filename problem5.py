def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

print reduce(lambda x, y: x*y//gcd(x,y), range(1,21))

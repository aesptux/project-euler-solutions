max = 0
for x in range(100,1000):
    for i in range(100,1000):
        n = x * i
        if n == int(str(n)[::-1]) and n > max:
            max = n
print max

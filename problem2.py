sum, a, b = 0, 1 ,2
while b < 4000000:
    if b % 2 == 0:
        sum = sum + b
    a, b = b, a+b
print sum

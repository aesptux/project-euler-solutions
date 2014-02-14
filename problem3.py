def prime(n, a):
  i = a
  while (n % i != 0 and i * i < n):
    i += 1
  if (i * i < n):
    return prime (n / i, i)
  else:
    print n

prime(600851475143, 2)
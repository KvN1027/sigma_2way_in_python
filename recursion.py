def sigma(n):
    if n == 100:
        return 100
    else:
        return n + sigma(n+1)


print(sigma())

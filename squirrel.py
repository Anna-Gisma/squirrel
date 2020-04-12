def squirrel(N):
    f = 1
    n = 1
    for i in range(1, N + 1):
        f *= i
        n = int(str(f)[0])
    return n
            


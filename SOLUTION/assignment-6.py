def star_pattern(n):
    for i in range(1, n+1):
        print(*map(lambda x: "*", range(i)))
from itertools import product
def alphabet_pattern(n):
    for i in range(1, n+1):
        print(*[chr(ord('A') + j - 1) for j in product(range(1, i+1), repeat=1)])
import pandas as pd
def triangle(n):
    for i in range(1, n+1):
        print(*pd.Series(range(1, i+1)))
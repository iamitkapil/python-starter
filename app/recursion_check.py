def solve(x):
    if x <= 1:
        return x
    if x % 2 == 0:
        return solve(x - 1) + solve(x - 2) + solve(x - 3)
    else:
        return solve(x - 1) * 2 + solve(x - 3)

def solve(x, depth=0):
    if x <= 0:
        return 1
    if depth > 5:
        return x + solve(x - 1, depth - 1)
    if x % 2 == 0:
        return (
            solve(x - 1, depth + 1) + 
            solve(x - 2, depth + 1) +
            solve(x - 3, depth + 2) +
            solve(x - 4, depth + 3)
        )
    else:
        return (
            solve(x - 1, depth + 2) * 2 - 
            solve(x - 3, depth + 1) +
            solve(x - 5, depth + 4)
        ) + solve(x // 2, depth + 3)

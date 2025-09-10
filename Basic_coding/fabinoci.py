def fibonacci_series(n):
    a, b = 0, 1  # Initialize the first two numbers
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b  # Update for the next iteration
    return series

print(fibonacci_series(1))
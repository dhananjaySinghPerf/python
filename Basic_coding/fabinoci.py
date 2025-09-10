def fibonacci_series(n):
    a, b = 0, 1  # Initialize the first two numbers
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b  # Update for the next iteration
    return series

ln = int(input("Enter the length of the sequesnce \n"))
print("The series is \n",fibonacci_series(ln))

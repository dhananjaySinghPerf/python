def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]
    
    return abs(primary_sum - secondary_sum)



n = int(input("enter the length of array \n").strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print("Difference of diagonal",result)

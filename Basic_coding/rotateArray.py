def rotateLeft(d, arr):
    n = len(arr)
    d = d % n  # To avoid unnecessary full cycles
    return arr[d:] + arr[:d]

def rotateRight(d, arr):
    n = len(arr)
    d = d % n  # To avoid unnecessary full cycles
    return arr[-d:] + arr[:-d]

d = 2
arr = [1,2,3,4,5]
print(rotateLeft(d,arr))
print(rotateRight(d,arr))
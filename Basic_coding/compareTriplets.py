
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
        # if equal, do nothing

    return [alice_score, bob_score]



#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
a = [1, 2, 3]
b = [3, 2, 1]
result = compareTriplets(a, b)
print(*result)
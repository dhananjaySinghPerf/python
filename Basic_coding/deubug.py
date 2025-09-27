from collections import defaultdict
# Reverse an array in place

a = ['a', 'b', 'c', 'd']
rev = []
for n in range(len(a) -1, -1, -1):
    rev.append(a[n])
    print(rev)

b = [9, 8, 4, 3]

rev = ''.join(sorted(rev))
print(rev)

print(rev.count('x'))
freq_map = defaultdict(int)

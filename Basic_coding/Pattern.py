b = {}

a = "nepleaww"
for n in a:
    print(b)
    b[n] = b.get(n,0) + 1
    
print(b)
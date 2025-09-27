def generate_substrings(s):
    substrings = []
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            key = ''.join(sorted(substr))
            print("Key",key)
            substrings.append(substr)
    
    return substrings

print(generate_substrings("abefe"))
#str = "abefe"
#print(str[1:1])
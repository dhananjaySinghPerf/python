from collections import defaultdict

def group_anagrams(strs):
    d = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        d[key].append(s)
    return list(d.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [['eat','tea','ate'], ['tan','nat'], ['bat']]


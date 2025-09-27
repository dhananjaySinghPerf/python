'''Two strings are anagrams of each other if the letters of one 
string can be rearranged to form the other string. Given a string, 
find the number of pairs of substrings of the string that are anagrams of each other.'''


from collections import defaultdict

def count_anagrammatic_pairs(s):
    freq_map = defaultdict(int)

    # Generate all substrings
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            key = ''.join(sorted(substr))  # Canonical form
            freq_map[key] += 1

    # Count pairs from frequency map
    count = 0
    for key in freq_map:
        freq = freq_map[key]
        if freq > 1:
            count += (freq * (freq - 1)) // 2  # nC2 pairs

    return count
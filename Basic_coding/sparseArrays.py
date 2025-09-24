def matchingStrings(stringList, queries):
    # Step 1: Count frequencies of strings in stringList
    freq = {}
    for s in stringList:
        freq[s] = freq.get(s, 0) + 1

    print(freq)
    # Step 2: Look up each query
    result = []
    for q in queries:
        print(freq.get(q, 0))
        result.append(freq.get(q, 0))

    return result



stringList = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]

print(matchingStrings(stringList, queries))
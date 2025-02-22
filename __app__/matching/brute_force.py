def brute_force(text, pattern):
    t = len(text)
    p = len(pattern)

    for i in range(t - p + 1):
        j = 0 
        while j < p and text[i + j] == pattern[j]:
            j += 1
        if j == p:
            return i
    return - 1
def shortest_to_char(s, c):
    n = len(s)
    result = [0] * n
    prev = float('-inf')

    # First pass: left to right
    for i in range(n):
        if s[i] == c:
            prev = i
        result[i] = i - prev

    # Second pass: right to left
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        result[i] = min(result[i], prev - i)

    return result


s = "lovecodewars"
c = "e"
print(shortest_to_char(s, c))
def maxConsecutive(bottom: int, top: int, special) -> int:
    n = len(special)
    special.sort()
    maxRange = max(special[0] - bottom, top - special[-1])

    for i in range(n-1):
        curr = special[i+1] - (special[i] + 1)
        maxRange = max(maxRange, curr)
    return maxRange


b = 2
t = 9
s = [4, 6]
print(maxConsecutive(b, t, s))

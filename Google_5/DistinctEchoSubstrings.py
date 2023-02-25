def distinctEchoSubstrings(text: str) -> int:
    n = len(text)
    count = 0
    seen = set()
    for k in range(1, n//2 + 1):
        seen.clear()
        for i in range(n - k):
            s1 = text[i:i+k]
            s2 = text[i+k:i+2*k]

            if s1 == s2 and s1 not in seen:
                count += 1
                seen.add(s1)
    return count


t = "leeleetleeleeleclec"
print(distinctEchoSubstrings(t))

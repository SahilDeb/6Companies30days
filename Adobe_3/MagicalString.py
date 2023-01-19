# Given an integer n, return the number of 1's in the first n number in the magical string s.
def magicalString(n: int) -> int:
    S = [1, 2, 2]
    idx = 2
    while len(S) < n:
        S += S[idx] * [(3 - S[-1])]
        idx += 1
    return S[:n].count(1)


print(magicalString(116))

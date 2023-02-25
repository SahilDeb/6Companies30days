def isStrictlyPalindromic(n: int) -> bool:
    def findBase(n, base):
        res = ""
        while n > 0:
            res += str(n % base)
            n //= base
        return res

    for b in range(2, n-1):
        res = findBase(n, b)
        if res != res[::-1]:
            return False
    return True


n = 78678
print(isStrictlyPalindromic(n))

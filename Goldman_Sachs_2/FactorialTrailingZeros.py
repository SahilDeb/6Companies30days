# O(log n)
def trailingZeroes(n: int) -> int:
    # 10 is formed using 2 and 5
    # but there is more multiple of 2 than 5 in any number
    # need to count the number of multiple of 5 in n
    # that will determine the 0s at the end

    cnt = 0
    while n > 0:
        cnt += n//5
        n //= 5

    return cnt


n = 2147483647
print(trailingZeroes(n))

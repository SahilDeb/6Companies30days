def findIntegers(num: int) -> int:
    # by observation we find that
    # for 2 elements, valid cases are = 00, 01, 10
    # for 3 elements, valid cases are = 000, 001, 010, 100, 101
    # so we see that for a case to be valid, it should either start with 0 or 10
    # so generalizing the equation, xxxx => 0xxx + 10xx
    # which is nothing but f(i) => f(i-1) + f(i-2)
    # thus fibonacci equation

    binary = bin(num)[2:]
    n = len(binary)

    # dp[i] = count of numbers for i num of digits which do not contain consecutive 1
    dp = [1, 2]
    for i in range(2, n):
        dp.append(dp[i - 1] + dp[i - 2])

    flag, ans = 0, 0
    for i in reversed(range(n)):
        # to check if ith bit of the num is set
        if (1 << i) & num:
            ans += dp[i]
            if flag:
                return ans
            flag = 1
        else:
            flag = 0

    return ans+1


n = 15
n = 13
print(findIntegers(n))

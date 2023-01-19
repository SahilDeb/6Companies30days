def fractionToDecimal(numerator: int, denominator: int) -> str:
    # 3 parts
    # 1. Division without fraction
    # 2. Division with fraction but no repeating number
    # 3. Division with fraction and repeating number

    if numerator == 0:
        return "0"

    a, b = abs(numerator), abs(denominator)
    ans = ""
    if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
        ans += "-"

    q, r = int(a/b), a % b
    ans += str(q)

    # part 1
    if r == 0:
        return ans

    ans += "."
    remMap = dict()

    while r != 0:
        # Part 3
        # For the 3rd part we need to use a dictionary
        # so that we can store the the position from where
        # the repeating of number starts in front of the remainder.
        # if the rem already in map, add "("
        if r in remMap:
            pos = remMap[r]
            ans = ans[:pos] + "(" + ans[pos:]
            ans += ")"
            break
        else:
            # Part 2
            # store the pos at which that remainder got added
            remMap[r] = len(ans)
            r *= 10
            q, r = int(r/b), r % b
            ans += str(q)

    return ans


a = -22
b = -242
print(fractionToDecimal(a, b))

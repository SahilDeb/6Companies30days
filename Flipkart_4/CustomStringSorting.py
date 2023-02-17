from collections import Counter


def customSortString(order: str, s: str) -> str:
    counterDict = Counter(s)

    res = ""
    for char in order:
        if char in counterDict:
            count = counterDict[char]
            res += (char * count)
            counterDict[char] = 0

    for char, count in counterDict.items():
        res += (char * count)

    return res


o = "cbafg"
s = "assabbaafqcc"
print(customSortString(o, s))

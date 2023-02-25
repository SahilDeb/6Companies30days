def totalFruit(fruits) -> int:
    n = len(fruits)
    maxFruits = 0
    taken = {}
    currCount = 0

    for i in range(n):
        if len(taken) == 2 and fruits[i] not in taken:
            # find the fruits which has the min idx
            key, idx = [(k, v) for k, v in taken.items()
                        if v == min(taken.values())][0]
            # update the max count
            maxFruits = max(maxFruits, currCount)
            # update the count of fruits after removal
            currCount = i - idx
            # remove that element
            taken.pop(key)
        else:
            currCount += 1
        # update the idx for fruits every iteration
        taken[fruits[i]] = i

    maxFruits = max(maxFruits, currCount)
    return maxFruits


f = [1, 2, 3, 2, 2]
print(totalFruit(f))

def maxScore(idx, arrows, currScore, scoreboard, aliceBoard, maxScore, res):
    if idx < 0:
        if currScore > maxScore[0]:
            maxScore[0] = currScore
            res.append(scoreboard[:])
        return

    # pick
    arrowsNeeded = aliceBoard[idx] + 1
    if arrows >= arrowsNeeded:
        old = scoreboard[idx]
        scoreboard[idx] = arrowsNeeded
        maxScore(idx - 1, arrows - arrowsNeeded, currScore +
                 idx, scoreboard, aliceBoard, maxScore, res)
        scoreboard[idx] = old

    # not pick
    maxScore(idx - 1, arrows, currScore, scoreboard, aliceBoard, maxScore, res)


def maximumBobPoints(numArrows: int, aliceArrows):
    # Backtracking
    # O(12 * 2^12)
    # res = []
    # bobArrows = [0]*12
    # maxScore(11, numArrows, 0, bobArrows, aliceArrows, [0], res)
    # res = res[-1]
    # # In case of having remain arrows then it means in all sections Bob always win
    # # then we can distribute the remain to any section, here we simple choose first section.
    # res[0] += numArrows - sum(res)
    # return res

    # DP Solution
    # top down approach
    # O (2 * 12 * numArrows)
    def dp(idx, arrows):
        if idx == 12 or arrows <= 0:
            return 0

        # not pick
        maxScore = dp(idx + 1, arrows)

        # pick
        if arrows > aliceArrows[idx]:
            res = idx + dp(idx + 1, arrows - (aliceArrows[idx] + 1))
            maxScore = max(maxScore, res)
        return maxScore

    bobArrows = [0]*12
    remainArrows = numArrows

    for idx in range(12):
        # that means bob won the idx position
        if dp(idx, numArrows) != dp(idx + 1, numArrows):
            bobArrows[idx] = aliceArrows[idx] + 1
            remainArrows -= bobArrows[idx]
            numArrows -= bobArrows[idx]

    # for remaining arrows
    bobArrows[0] += remainArrows
    return bobArrows

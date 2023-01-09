# Logic is to find slope of 2 given points
# and count the number of points on same slope and keep track of maximum points on a slope
# formula for slope => y2 - y1 / x2 - x1
def maxPoints(points) -> int:
    n = len(points)
    INT_MAX = int(1e04+1)

    # if less than equal to 2 points, then only 1 line can be formed so all points included
    if n <= 2:
        return n

    res = 0
    for i in range(n-1):
        # re-initialize the slope dict every iteration
        # initialize the dict with the corner case of infinite slope line i.e. if x coord of 2 points is same but not y coord
        slopeFreq = {INT_MAX: 1}
        # keep track of 2 same coord points
        overlap = 0
        for j in range(i+1, n):
            x = float(points[i][0] - points[j][0])
            y = float(points[i][1] - points[j][1])

            # same point
            if x == 0 and y == 0:
                overlap += 1
                continue

            # if x is same for both points, results to a positive infinite slope.
            if x == 0:
                slope = INT_MAX
            else:
                slope = y / x

            # check if slope is there in dict
            if slope not in slopeFreq:
                slopeFreq[slope] = 1

            # increase the number of points for that slope
            slopeFreq[slope] += 1

        # keep track of max points acheived for a slope
        res = max(res, max(slopeFreq.values()) + overlap)

    return res


p1 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
p2 = [[1, 1], [2, 2], [3, 3]]
print(maxPoints(p2))

# calculate dist between 2 points
def getDist(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

# permutations of nP2


def getCount(n):
    return n * (n - 1)

# logic is to keep track of number of pairs which has the same distance between them
# then boomerang count will be nP2 of that pair count

# O(N^2)


def numberOfBoomerangs(points) -> int:
    n = len(points)
    boomCount = 0
    distFreq = dict()
    for i in range(n):
        distFreq.clear()
        for j in range(n):
            if j == i:
                continue

            d = getDist(points[i], points[j])
            if d not in distFreq:
                distFreq[d] = 1
            else:
                distFreq[d] += 1

        for v in distFreq.values():
            boomCount += getCount(v)

    return boomCount


p = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
print(numberOfBoomerangs(p))

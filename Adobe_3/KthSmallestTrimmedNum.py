def smallestTrimmedNumbers(nums, queries):
    heapDict = {}

    res = []
    for k, t in queries:
        if t not in heapDict:
            heapDict[t] = sorted([(num[-t:], i) for i, num in enumerate(nums)])

        idx = heapDict[t][k - 1][1]
        res.append(idx)
    return res


n = ["64333639502", "65953866768", "17845691654", "87148775908", "58954177897", "70439926174", "48059986638",
     "47548857440", "18418180516", "06364956881", "01866627626", "36824890579", "14672385151", "71207752868"]
q = [[9, 4], [6, 1], [3, 8], [12, 9], [11, 4], [4, 9],
     [2, 7], [10, 3], [13, 1], [13, 1], [6, 1], [5, 10]]

print(smallestTrimmedNumbers(n, q))

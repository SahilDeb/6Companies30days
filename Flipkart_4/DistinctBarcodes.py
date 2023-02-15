from collections import Counter


def rearrangeBarcodes(barcodes):
    n = len(barcodes)

    if n == 1:
        return barcodes

    res = [0]*n

    # get the list of tuples of (val, freq) in increasing order
    cnt = Counter(barcodes).most_common()[::-1]
    # put all the values to be added in a list in increasing order of freq
    ref = [val for val, t in cnt for _ in range(t)]

    # fill the even positions
    for i in range(0, len(barcodes), 2):
        res[i] = ref.pop()

    # fill the odd positions
    for i in range(1, len(barcodes), 2):
        res[i] = ref.pop()
        # print(res)
    return res


b = [7, 7, 7, 8, 5, 7, 5, 5, 5, 8]
print(rearrangeBarcodes(b))

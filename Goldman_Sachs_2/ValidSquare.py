# formula for getting length between 2 points
# d^2 = (x2 - x1)^2 + (y2 - y1)^2
def getLength(p1, p2):
    return (p2[1] - p1[1])**2 + (p2[0] - p1[0])**2

# the logic is to find length of all combinations of those 4 points
# sort them to get smallest equal lengths in the start and length of diagonals in the end
# if length of 4 sides are EQUAL and length of 2 diagonals are EQUAL and length of diagonal = 2 * length of side
# it's a SQUARE


def validSquare(p1, p2, p3, p4) -> bool:
    if p1 == p2 == p3 == p4:
        return False

    # calculate length between all combination of points
    sizes = [getLength(p1, p2), getLength(p1, p3), getLength(
        p1, p4), getLength(p2, p3), getLength(p2, p4), getLength(p3, p4)]

    # sort them to get the minimum and equal lengths together
    sizes.sort()

    # check for length equality
    if sizes[0] == sizes[1] == sizes[2] == sizes[3]:
        # the length of diagonals should be same too
        if sizes[4] == sizes[5] and sizes[4] == 2 * sizes[0]:
            return True
    return False


P1 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
P2 = [[0, 0], [1, 1], [1, 0], [0, 12]]
print(validSquare(*P2))

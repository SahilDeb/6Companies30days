# The right answer must satisfy two conditions:

# 1. the large rectangle area should be equal to the sum of small rectangles
# 2. We should be able to find 4 corner points which is the bounding box for merged rectangles

# The key point becomes whether there are overlapped areas.
# Every corner point of a rectangle is shared by 2 or 4 small rectangles, except the 4 corner points of the bounding rectangle.
# So we traverse all the rectangles,
# if the corner point exits, delete it from the set(O(1)), else add it to the set.
# If there are 4 corner points, it means no overlapped area is found, and we can compare the total area.

def isRectangleCover(rectangles) -> bool:
    # set to store all points of the bounding box
    corner_point = set()
    # Total area of all sub rectangles should be equal to larger bounding rectangle
    totalArea = 0
    for x, y, a, b in rectangles:
        totalArea += (a - x) * (b - y)

        # So we traverse all points the rectangles,
        # if the corner point exists, delete it from the set(O(1))
        # else add it to the set.
        # If there are 4 corner points, it means no overlapped area is found,
        # and we can compare the total area.
        for point in [(x, y), (a, y), (a, b), (x, b)]:
            if point in corner_point:
                corner_point.remove(point)
            else:
                corner_point.add(point)

    # more than 4 indicates spaced or overlapping rectangle
    if len(corner_point) != 4:
        return False

    # sort the last 4 corner points
    # the first point is the bottom left point,
    # and the last point is the top right point.
    corner_point = sorted(list(corner_point), key=lambda x: (x[0], x[1]))
    print(corner_point)
    return totalArea == ((corner_point[-1][0]-corner_point[0][0])*(corner_point[-1][1]-corner_point[0][1]))


t1 = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
t2 = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
t3 = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
t4 = [[0, 0, 1, 1], [0, 0, 2, 1], [1, 0, 2, 1], [0, 2, 2, 3]]

print(isRectangleCover(t1))

# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point
from plotting import plot_points, draw_hull, title, show_plot


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    points.sort(key=lambda point: point[0])
    convex_linked_list = find_convex_hull(points)
    return convert_linked_list_to_tuples(convex_linked_list)

def convert_linked_list_to_tuples(linked_list) -> list[tuple[float, float]]:
    tuple_list = list[tuple[float, float]]()
    for point in linked_list:
        tuple_list.append((point.x, point.y))
    return tuple_list

def find_convex_hull(points: list[tuple[float, float]]):
    n = len(points)
    if n == 1:
        new_point = ConvexPoint(points[0][0], points[0][1])
        new_point.set_clockwise_neighbor(new_point)
        new_point.set_counterclockwise_neighbor(new_point)
        return [new_point]

    left = points[:(n//2)]
    right = points[(n//2):]

    left_convex_hull = find_convex_hull(left)
    right_convex_hull = find_convex_hull(right)


    rightmost_point = find_rightmost_point(left_convex_hull)
    leftmost_point = find_leftmost_point(right_convex_hull)

    upper_left, upper_right = find_upper_tangent(leftmost_point, rightmost_point)
    lower_left, lower_right = find_lower_tangent(leftmost_point, rightmost_point)

    return merge_convex_hulls(left_convex_hull, right_convex_hull, upper_left, upper_right, lower_left, lower_right)


def find_leftmost_point(convex_hull):
    leftmost = None
    for point in convex_hull:
        if point.c_neighbor is not None and point.cc_neighbor is not None:
            if leftmost is None:
                leftmost = point
            else:
                if point.x < leftmost.x:
                    leftmost = point
    return leftmost

def find_rightmost_point(convex_hull):
    rightmost = None
    for point in convex_hull:
        if point.c_neighbor is not None and point.cc_neighbor is not None:
            if rightmost is None:
                rightmost = point
            else:
                if point.x > rightmost.x:
                    rightmost = point
    return rightmost

def find_upper_tangent(leftmost_point, rightmost_point):
    temp_left = rightmost_point
    temp_right = leftmost_point

    change_count = 1
    while change_count != 0:
        change_count = 0
        while calculate_slope(temp_left, temp_right) > calculate_slope(temp_left.cc_neighbor, temp_right):
            temp_left = temp_left.cc_neighbor
            change_count += 1
        while calculate_slope(temp_left, temp_right) < calculate_slope(temp_left, temp_right.c_neighbor):
            temp_right = temp_right.c_neighbor
            change_count += 1

    return temp_left, temp_right

def find_lower_tangent(leftmost_point, rightmost_point):
    temp_left = rightmost_point
    temp_right = leftmost_point

    change_count = 1
    while change_count != 0:
        change_count = 0
        while calculate_slope(temp_left, temp_right) < calculate_slope(temp_left.c_neighbor, temp_right):
            temp_left = temp_left.c_neighbor
            change_count += 1
        while calculate_slope(temp_left, temp_right) > calculate_slope(temp_left, temp_right.cc_neighbor):
            temp_right = temp_right.cc_neighbor
            change_count += 1

    return temp_left, temp_right

def calculate_slope(left_point, right_point):
    return (right_point.y - left_point.y) / (right_point.x - left_point.x)

def merge_convex_hulls(left_convex_hull, right_convex_hull, upper_left, upper_right, lower_left, lower_right):
    new_convex_hull = []
    for l_point in left_convex_hull:
        if l_point.x == upper_left.x and l_point.y == upper_left.y:
            for r_point in right_convex_hull:
                if r_point.x == upper_right.x and r_point.y == upper_right.y:
                    l_point.set_clockwise_neighbor(r_point)
                    r_point.set_counterclockwise_neighbor(l_point)
                    new_convex_hull.append(l_point)
                    new_convex_hull.append(r_point)
        if l_point.x == lower_left.x and l_point.y == lower_left.y:
            for r_point in right_convex_hull:
                if r_point.x == lower_right.x and r_point.y == lower_right.y:
                    l_point.set_counterclockwise_neighbor(r_point)
                    r_point.set_clockwise_neighbor(l_point)

    next_point = new_convex_hull[1]
    while next_point != new_convex_hull[0]:
        if next_point != new_convex_hull[1]:
            new_convex_hull.append(next_point)
        next_point = next_point.c_neighbor

    return new_convex_hull


class ConvexPoint:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
        self.c_neighbor = None
        self.cc_neighbor = None

    def set_counterclockwise_neighbor(self, cc_neighbor):
        self.cc_neighbor = cc_neighbor

    def set_clockwise_neighbor(self, c_neighbor):
        self.c_neighbor = c_neighbor

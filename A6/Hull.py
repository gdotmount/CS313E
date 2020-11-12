
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)


def det (p, q, r):
    return q.x * r.y - q.y * r.x - p.x * (r.y - q.y) + p.y * (r.x - q.x)


def convex_hull(sorted_points):
    upper_hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-1], upper_hull[-2]) <= 0:
            upper_hull.pop(-2)
    lower_hull = [sorted_points[-1], sorted_points[-2]]
    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-1], lower_hull[-2]) <= 0:
            lower_hull.pop(-2)
    lower_hull.pop(0)
    lower_hull.pop(-1)
    return upper_hull + lower_hull


def area_poly(convex_poly):
    convex_poly.append(convex_poly[0])
    determinant = 0
    for i in range(0, len(convex_poly) - 1):
        determinant += (convex_poly[i].x * convex_poly[i+1].y - convex_poly[i].y * convex_poly[i+1].x)
    return 0.5 * abs(determinant)


def main():
    points = []
    n = int(input())
    for ind in range(n):
        point = input().split()
        point = Point(int(point[0]), int(point[1]))
        points.append(point)
    points.sort(key=lambda p: p.y)
    points.sort(key=lambda p: p.x)
    hull = convex_hull(points)
    print('Convex Hull')
    [print(p) for p in hull]
    print()
    print(f'Area of Convex Hull: {area_poly(hull)}')


if __name__ == "__main__":
    main()

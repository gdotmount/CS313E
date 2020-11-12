import math


class Point(object):
    # constructor with default values
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        return (abs(self.x - other.x) < 1.0e-6
                and abs(self.y - other.y) < 1.0e-6
                and abs(self.z - other.z) < 1.0e-6)


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=1.0):
        self.center = Point(x, y, z)
        self.radius = radius
        self.axes = {
            'x_max': self.center.x + self.radius,
            'x_min': self.center.x - self.radius,
            'y_max': self.center.y + self.radius,
            'y_min': self.center.y - self.radius,
            'z_max': self.center.z + self.radius,
            'z_min': self.center.z - self.radius
        }

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return f'Center: {self.center.__str__}, Radius: {self.radius}'

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * self.radius ** 2

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return self.center.distance(p) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        return self.center.distance(other.center) + other.radius < self.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are inside
    # the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        return False not in [self.center.distance(vertex) < self.radius
                             for vertex in a_cube.vertices.values()]

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        if a_cyl.center.z >= self.center.z and a_cyl.center.z + a_cyl.height / 2 < self.center.z + self.radius:
            center_elevation = a_cyl.center.z - self.center.z + a_cyl.height / 2
            elevated_circular_r = math.sqrt(self.radius ** 2 - center_elevation ** 2)
            elevated_center = Point(self.center.x, self.center.y, a_cyl.center.z + a_cyl.height / 2)
            elevated_cylinder_center = Point(a_cyl.center.x, a_cyl.center.y, a_cyl.center.z + a_cyl.height / 2)
            return elevated_center.distance(elevated_cylinder_center) + a_cyl.radius < elevated_circular_r

        elif a_cyl.center.z < self.center.z and a_cyl.center.z - a_cyl.height / 2 > self.center.z - self.radius:
            center_declination = self.center.z - a_cyl.center.z + a_cyl.height / 2
            declinated_circular_r = math.sqrt(self.radius ** 2 - center_declination ** 2)
            declinated_center = Point(self.center.x, self.center.y, a_cyl.center.z - a_cyl.height / 2)
            declinated_cylinder_center = Point(a_cyl.centert.x, a_cyl.center.y, a_cyl.center.z - a_cyl.height / 2)
            return declinated_center.distance(declinated_cylinder_center) + a_cyl.radius < declinated_circular_r
        return False

    # determine if another Sphere intersects this Sphere
    # there is a non-zero volume of intersection
    # other is a Sphere object
    # returns a Boolean
    def does_intersect_sphere(self, other):
        return (not self.is_inside_sphere(other)
                and not other.is_inside_sphere(self)
                and self.center.distance(other.center) < self.radius + other.radius)

    # determine if a Cube intersects this Sphere
    # there is a non-zero volume of intersection
    # there is at least one corner of the Cube in
    # the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        return (self.axes['x_min'] <= a_cube.axes['x_min'] <= self.axes['x_max'] <= a_cube.axes['x_max']
                or a_cube.axes['x_min'] <= self.axes['x_min'] <= a_cube.axes['x_max'] <= self.axes['x_max']
                or self.axes['y_min'] <= a_cube.axes['y_min'] <= self.axes['x_max'] <= a_cube.axes['x_max']
                or a_cube.axes['y_min'] <= self.axes['y_min'] <= a_cube.axes['y_max'] <= a_cube.axes['y_max']
                or self.axes['z_min'] <= a_cube.axes['z_min'] <= self.axes['z_max'] <= a_cube.axes['z_max']
                or a_cube.axes['z_min'] <= self.axes['z_min'] <= a_cube.axes['z_max'] <= self.axes['z_max'])

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        return Cube(self.center.x, self.center.y, self.center.z, (2 / 3) * math.sqrt(3) * self.radius)


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0.0, y=0.0, z=0.0, side=1.0):
        self.center = Point(x, y, z)
        self.side = side
        increment = side / 2
        self.axes = {
            'x_max': x + increment,
            'x_min': x - increment,
            'y_max': y + increment,
            'y_min': y - increment,
            'z_max': z + increment,
            'z_min': z - increment
        }
        self.vertices = {
            '+x+y+z': Point(x + increment, y + increment, z + increment),
            '-x+y+z': Point(x - increment, y + increment, z + increment),
            '+x-y+z': Point(x + increment, y - increment, z + increment),
            '+x+y-z': Point(x + increment, y + increment, z - increment),
            '-x-y+z': Point(x - increment, y - increment, z + increment),
            '-x+y-z': Point(x - increment, y + increment, z - increment),
            '+x-y-z': Point(x + increment, y - increment, z - increment),
            '-x-y-z': Point(x - increment, y - increment, z - increment)
        }

        # string representation of a Cube of the form:

    # Center: (x, y, z), Side: value
    def __str__(self):
        return f'Center: {self.center.__str__}, Side: {self.side}'

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * self.side ** 2

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        return (self.axes['x_min'] < p.x < self.axes['x_max']
                and self.axes['y_min'] < p.y < self.axes['y_max']
                and self.axes['z_max'] < p.z < self.axes['z_min'])

    # determine if a Sphere is strictly inside this Cube or
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        return (self.axes['x_max'] > a_sphere.axes['x_max']
                and self.axes['x_min'] < a_sphere.axes['x_min']
                and self.axes['y_max'] > a_sphere.axes['y_max']
                and self.axes['y_min'] < a_sphere.axes['y_min']
                and self.axes['z_max'] > a_sphere.axes['z_max']
                and self.axes['z_min'] < a_sphere.axes['z_min'])

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        return (self.axes['x_min'] < other.axes['x_min']
                and self.axes['x_max'] > other.axes['x_max']
                and self.axes['y_min'] < other.axes['y_min']
                and self.axes['y_max'] > other.axes['y_max']
                and self.axes['z_min'] < other.axes['z_min']
                and self.axes['z_max'] > other.axes['z_max'])

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        return (self.axes['x_max'] > a_cyl.center.x + a_cyl.radius
                and self.axes['x_min'] < a_cyl.center.x - a_cyl.radius
                and self.axes['y_max'] > a_cyl.center.y + a_cyl.radius
                and self.axes['y_min'] < a_cyl.center.y - a_cyl.radius
                and self.axes['z_max'] > a_cyl.center.z + a_cyl.height / 2
                and self.axes['z_min'] < a_cyl.center.z - a_cyl.height / 2)

    # determine if another Cube intersects this Cube
    # there is a non-zero volume of intersection
    # there is at least one vertex of the other Cube
    # in this Cube
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        return (self.axes['x_min'] <= other.axes['x_min'] <= self.axes['x_max'] <= other.axes['x_max']
                or other.axes['x_min'] <= self.axes['x_min'] <= other.axes['x_max'] <= self.axes['x_max']
                or self.axes['y_min'] <= other.axes['y_min'] <= self.axes['y_max'] <= other.axes['y_max']
                or other.axes['y_min'] <= self.axes['y_min'] <= other.axes['y_max'] <= self.axes['y_max']
                or self.axes['z_min'] <= other.axes['z_min'] <= self.axes['z_max'] <= other.axes['z_max']
                or other.axes['z_min'] <= self.axes['z_min'] <= other.axes['z_max'] <= self.axes['z_max'])

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        if self.does_intersect_cube(other):
            if (self.center.x <= other.center.x
                    and self.center.y <= other.center.y
                    and self.center.z <= other.center.z):
                return ((self.axes['x_max'] - other.axes['x_min'])
                        * (self.axes['y_max'] - other.axes['y_min'])
                        * (self.axes['z_max'] - other.axes['z_min']))
            elif (self.center.x <= other.center.x
                  and self.center.y >= other.center.y
                  and self.center.z <= other.center.z):
                return ((self.axes['x_max'] - other.axes['x_min'])
                        * (other.axes['y_max'] - other.axes['y_min'])
                        * (self.axes['z_max'] - other.axes['z_min']))
            elif (self.center.x >= other.center.x
                  and self.center.y >= other.center.y
                  and self.center.z <= other.center.z):
                return ((other.axes['x_max'] - self.axes['x_min'])
                        * (other.axes['y_max'] - self.axes['y_min'])
                        * (self.axes['z_max'] - other.axes['z_min']))
            elif (self.center.x >= other.center.x
                  and self.center.y <= other.center.y
                  and self.center.z <= other.center.z):
                return ((other.axes['x_max'] - self.axes['x_min'])
                        * (self.axes['y_max'] - other.axes['y_min'])
                        * (self.axes['z_max'] - other.axes['z_min']))
            elif (self.center.x <= other.center.x
                  and self.center.y <= other.center.y
                  and self.center.z >= other.center.z):
                return ((self.axes['x_max'] - other.axes['x_min'])
                        * (self.axes['y_max'] - other.axes['y_min'])
                        * (other.axes['z_max'] - self.axes['z_min']))
            elif (self.center.x <= other.center.x
                  and self.center.y >= other.center.y
                  and self.center.z >= other.center.z):
                return ((self.axes['x_max'] - other.axes['x_min'])
                        * (other.axes['y_max'] - self.axes['y_min'])
                        * (other.axes['z_max'] - self.axes['z_min']))
            elif (self.center.x >= other.center.x
                  and self.center.y >= other.center.y
                  and self.center.z >= other.center.z):
                return ((other.axes['x_max'] - self.axes['x_min'])
                        * (other.axes['y_max'] - self.axes['y_min'])
                        * (other.axes['z_max'] - self.axes['z_min']))
            elif (self.center.x >= other.center.x
                  and self.center.y <= other.center.y
                  and self.center.z >= other.center.z):
                return ((other.axes['x_max'] - self.axes['x_min'])
                        * (self.axes['y_max'] - other.axes['y_min'])
                        * (other.axes['z_max'] - self.axes['z_min']))
        return 0.0

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side / 2)


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=1.0, height=1.0):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return f'''Center: ({self.center.x}, {self.center.y}, {self.center.z}), 
                   Radius: {self.radius}, 
                   Height: {self.height}'''

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return (self.center.z - self.height / 2 < p.z < self.center.z + self.height / 2
                and self.center.distance(p) < self.radius)

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        return (self.center.distance(a_sphere.center) + a_sphere.radius < self.radius
                and a_sphere.axes['z_max'] < self.center.z + self.height / 2
                and a_sphere.axes['z_min'] > self.center.z - self.height / 2)

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are in
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        return (False not in ([Point(self.center.x, self.center.y, a_cube.axes['z_max']).distance(point) < self.radius
                               for point in (a_cube.vertices['+x+y+z'], a_cube.vertices['+x-y+z'],
                                             a_cube.vertices['-x-y+z'], a_cube.vertices['-x+y+z'])])
                and self.center.z + self.height / 2 > a_cube.axes['z_max']
                and self.center.z - self.height / 2 < a_cube.axes['z_min'])

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        return (Point(self.center.x, self.center.y, other.center.z).distance(other.center) + other.radius < self.radius
                and self.center.z + self.height / 2 > other.center.z + other.height / 2
                and self.center.z - self.height / 2 < other.center.z - other.height / 2)

    # determine if another Cylinder intersects this Cylinder
    # there is a non-zero volume of intersection
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        return (Point(self.center.x, self.center.y, other.center.z).distance(other.center) < self.radius + other.radius
                and not self.is_inside_cylinder(other)
                and not other.is_inside_cylinder(self)
                and (self.center.z - self.height / 2
                     <= other.center.z - other.height / 2
                     <= self.center.z + self.height / 2
                     <= other.center.z + other.height / 2
                     or other.center.z - other.height / 2
                     <= self.center.z - self.height / 2
                     <= other.center.z + other.height / 2
                     <= self.center.z + self.height / 2))


def main():
    def coords(): return [float(coord) for coord in input().split()]

    p_coords = coords()
    p = Point(p_coords[0], p_coords[1], p_coords[2])
    q_coords = coords()
    q = Point(q_coords[0], q_coords[1], q_coords[2])
    sphereA_attrs = coords()
    sphereA = Sphere(sphereA_attrs[0], sphereA_attrs[1], sphereA_attrs[2], sphereA_attrs[3])
    sphereB_attrs = coords()
    sphereB = Sphere(sphereB_attrs[0], sphereB_attrs[1], sphereB_attrs[2], sphereB_attrs[3])
    cubeA_attrs = coords()
    cubeA = Cube(cubeA_attrs[0], cubeA_attrs[1], cubeA_attrs[2], cubeA_attrs[3])
    cubeB_attrs = coords()
    cubeB = Cube(cubeB_attrs[0], cubeB_attrs[1], cubeB_attrs[2], cubeB_attrs[3])
    cylA_attrs = coords()
    cylA = Cylinder(cylA_attrs[0], cylA_attrs[1], cylA_attrs[2], cylA_attrs[3], cylA_attrs[4])
    cylB_attrs = coords()
    cylB = Cylinder(cylB_attrs[0], cylB_attrs[1], cylB_attrs[2], cylB_attrs[3], cylB_attrs[4])

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    print('Distance of Point p from the origin %s greater than the distance of Point q from the origin'
          % ('is' if Point().distance(p) > Point().distance(q) else 'is not'), end='\n\n')
    # print if Point p is inside sphereA
    print('Point p %s inside sphereA'
          % ('is' if sphereA.is_inside_point(p) else 'is not'))
    # print if sphereB is inside sphereA
    print('sphereB %s inside sphereA'
          % ('is' if sphereA.is_inside_sphere(sphereB) else 'is not'))
    # print if cubeA is inside sphereA
    print('cubeA %s inside sphereA'
          % ('is' if sphereA.is_inside_cube(cubeA) else 'is not'))
    # print if cylA is inside sphereA
    print('cylA %s inside sphereA'
          % ('is' if sphereA.is_inside_cyl(cylA) else 'is not'))
    # print if sphereA intersects with sphereB
    print('sphereA %s intersect sphereB'
          % ('does' if sphereB.does_intersect_sphere(sphereA) else 'does not'))
    # print if cubeB intersects with sphereB
    print('cubeB %s intersect sphereB'
          % ('does' if sphereB.does_intersect_cube(cubeB) else 'does not'))
    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    print('Volume of the largest Cube that is circumscribed by sphereA %s greater than the volume of cylA'
          % ('is' if sphereA.circumscribe_cube().volume() > cylA.volume() else 'is not'), end='\n\n')
    # print if Point p is inside cubeA
    print('Point p %s inside cubeA'
          % ('is' if cubeA.is_inside_point(p) else 'is not'))
    # print if sphereA is inside cubeA
    print('sphereA %s inside cubeA'
          % ('is' if cubeA.is_inside_sphere(sphereA) else 'is not'))
    # print if cubeB is inside cubeA
    print('cubeB %s inside cubeA'
          % ('is' if cubeA.is_inside_cube(cubeB) else 'is not'))
    # print if cylA is inside cubeA
    print('cylA %s inside cubeA'
          % ('is' if cubeA.is_inside_cylinder(cylA) else 'is not'))
    # print if cubeA intersects with cubeB
    print('cubeA %s intersect cubeB'
          % ('does' if cubeB.does_intersect_cube(cubeA) else 'does not'))
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    print('Intersection volume of cubeA and cubeB %s greater than the volume of sphereA'
          % ('is' if cubeA.intersection_volume(cubeB) > sphereA.volume() else 'is not'))
    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    print('Surface area of the largest Sphere object inscribed by cubeA %s greater than the surface area of cylA'
          % ('is' if cubeA.inscribe_sphere().area() > cylA.area() else 'is not'), end='\n\n')
    # print if Point p is inside cylA
    print('Point p %s inside cylA'
          % ('is' if cylA.is_inside_point(p) else 'is not'))
    # print if sphereA is inside cylA
    print('sphereA %s inside cylA'
          % ('is' if cylA.is_inside_sphere(sphereA) else 'is not'))
    # print if cubeA is inside cylA
    print('cubeA %s inside cylA'
          % ('is' if cylA.is_inside_cube(cubeA) else 'is not'))
    # print if cylB is inside cylA
    print('cylB %s inside cylA'
          % ('is' if cylA.is_inside_cylinder(cylB) else 'is not'))
    # print if cylB intersects with cylA
    print('cylB %s intersect cylA'
          % ('does' if cylA.does_intersect_cylinder(cylB) else 'does not'))


if __name__ == "__main__":
    main()

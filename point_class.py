class Point:
    """Create a coordinate points with values x and y on 2d plane"""

    def __init__(self, x: float, y: float) -> None:
        """constructor of a point object with x, y coordinates.
        Args:
        x(float): value of horizantal axis
        y (float): value of vertical axis.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x, self.y}"

    def get_location(self):
        return f"x:{self.x} \ny:{self.y}"

    def move_x(self, a: float) -> str:
        """Move a point in x coordinate

        args:
        a (float): distance to move from x direction

        returns:
        location(x+a, y) : new location of the point
        """
        return f"({self.x+a , self.y})"

    def move_y(self, a: float) -> str:
        """Move a point in y coordinate

        args:
        a (float): distance to move from y direction

        returns:
        location(x, y+a) : new location of the point
        """
        return f"({self.x, self.y+a})"

    def __add__(self, another) -> tuple:
        """add a point (x1, y1) to existing point(x2, y2)

        Args:
        a(tuple) :other point object
        returns:
        tuple : new point after addition"""
        return (self.x + another.x, self.y + another.y)


# instantiating point class
p1 = Point(2, 2)
p2 = Point(5, 6)

# The str representation of the points (__str__ method)
print(p1)
print(p2)

# Calling 'get_location' method
print(p1.get_location())
print(p2.get_location())

# Move point p1, 5 points in x-direction
print(p1.move_x(5))
# Move point p2, 4 points in y-direction
print(p2.move_y(5))


print(p1 + p2)

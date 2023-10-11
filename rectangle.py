class Rectangle:
    num_of_sides = 4
    num_of_diagonals = 2

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    @classmethod
    def instantiate_square(cls, side):
        return cls(side, side)

    def is_square(self):
        if Rectangle.is_quadrilateral():
            if self.length == self.width:
                return True
        return False

    @classmethod
    def is_quadrilateral(cls):
        if cls.num_of_sides == 4:
            return True
        else:
            return False

    @classmethod
    def get_num_of_joining_lines(cls) -> int:
        return cls.num_of_sides + cls.num_of_diagonals

    @staticmethod
    def rectangle_formulae() -> None:
        print("Area of length x width")
        print("Perimeter: 2*(length + width)")
        print("Diagonal: square root (square_of_length + square_of_width)")


# # Instantiate the Rectangle class (create a new rectangle object)
# rec1 = Rectangle(7, 4)

# # print area and perimeter of rec1
# print(rec1.area())
# print(rec1.perimeter())

# rec2 = Rectangle(12, 8)
# print(rec2.area())
# print(rec2.perimeter())

# Rectangle.num_of_sides = 5
# print(Rectangle.is_rectangle())
# print(Rectangle.get_joining_lines())
sq = Rectangle.instantiate_square(6)
print(sq.area())
print(sq.perimeter())

print(sq.is_quadrilateral())
print(Rectangle.rectangle_formulae())

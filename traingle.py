class Triangle:
    # def __init__(self):
    #     self.length = 3
    #     self.width = 4
    #     self.height = 5

    def __init__(self, length=3, width=4, height=5):
        self.length = length
        self.width = width
        self.height = height

    def get_area(self):
        return self.length * self.width * self.height

    def get_perimeter(self):
        return self.length + self.width + self.height


default_traingle = Triangle()
print(default_traingle.get_area())
print(default_traingle.get_perimeter())
custom_traingle = Triangle(4, 5, 6)
print(custom_traingle.get_area())
print(custom_traingle.get_perimeter())

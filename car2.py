""" classes : Car , DieselCar, ElectricCar
class Car:
instance variables: color, year, price, model
class variable : discount_precentage, year 
instance method : get_car_price, display_car_details, is_small_car
class method : change_discount_percentage, change_manufacturing_precentage

class DieselCar
instance variable : 
class variable : engine_type
instance method
class method:

class Electric car:

"""


class Car:
    """Car class for variety of engine types"""

    discount_percentage = 0.1

    def __init__(self, color, price, year, dimension=None) -> None:
        self.year = year
        self.color = color
        self.price = price
        if dimension is None:
            self.dimension = (None, None, None)
        else:
            self.dimension = dimension
        assert isinstance(self.dimension, tuple)
        assert len(self.dimension) == 3

    def display_details(self):
        """Display car details
        returns:
        dictionary containing car details"""
        car = {
            "color": self.color,
            "year": self.year,
            "price": self.price,
            "dimension": self.dimension,
        }
        return car

    @property
    def discounted_amount(self):
        """Calculate the discount amount
        returns:
        float : discount amount"""
        return self.price * self.discount_percentage

    @property
    def length(self):
        """doc string"""
        return self.dimension[0]

    @property
    def width(self):
        return self.dimension[2]

    @property
    def height(self):
        return self.height[3]

    def discounted_price(self):
        return self.price - self.discounted_amount

    def is_small_car(self):
        decider_length = 3800
        return True if self.length < decider_length else False

    @classmethod
    def set_discount_percentage(cls, percent):
        cls.discount_percentage = percent


class DieselCar(Car):
    fuel_type = "Diesel"

    def __init__(self, color, year, price, dimension=None, injector=4):
        super().__init__(color, price, year, dimension)
        self.injector = injector


class ElectricCar(Car):
    pass


if __name__ == "__main__":
    dcar_1 = DieselCar("white", 2023, 1500000, (4500, 1200, 1300), 4)
    car1 = Car("black", 2022, 1000000, (4500, 1100, 4567))
    car2 = Car("grey", 2022, 1100000, (3700, 1000, 1100))
    print(car1.discount_percentage)
    print(car2.discount_percentage)

    Car.set_discount_percentage(0.15)
    print(car1.discount_percentage)

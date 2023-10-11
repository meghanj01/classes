""" Car class: where each object has :
instance variables : mode, year, speed
class variables : MAKE, year
instance methods : get_speed, accelerate, apply_break, description
class methods: change year"""


class Car:
    """Car class for all the models of the car company"""

    make = "TATA Motors"
    year = 2022

    def __init__(self, model: str, category: str, speed: int) -> None:
        """Constructor for setting model , category and spee
        Args:
        model (string): model of the car
        category (string) : name of the category of the car
        speed (int): speed og the car"""
        self.model = model
        self.category = category
        self.speed = speed
        self.__private = 20

    def get_speed(self) -> str:
        return f"The max speed of {Car.make} is {self.speed} km/h"

    def acclerate(self) -> str:
        return " The vehicle is accelerating"

    def apply_break(self) -> str:
        return " The vehicle is de-accelerating"

    def description(self) -> None:
        print("==========================================")
        print(f"Company name: {Car.make}")
        print(f"Model: {self.model}")
        print(f"Category: {self.category}")
        print(f"Max Speed: {self.speed}")
        print(f"Manufacturing Year: {Car.year}")
        print()

    def __str__(self) -> str:
        print("==========================================")
        return f"Company name: {Car.make} \n Model: {self.model} \n Category: {self.category} \n \
Max Speed: {self.speed}\n Manufacturing Year: {Car.year}\n"

    @classmethod
    def change_year(cls, new_year):
        cls.year = new_year
        return cls.year


car1 = Car("Altroz", "Hatchback", 160)


car2 = Car("Nexon", "Compact SUV", 160)
car3 = Car("Safari", "MUV", 170)
car4 = Car("Harrier", "SUV", 180)
car1.description()
car2.description()
car3.description()
car4.description()
print(car1.get_speed())

year = Car.change_year(2023)
print(year)
print(car1.year)
print(car2.year)

print(dir(car1))
print(dir(Car))

print(car1._Car__private)
print(car1.__dict__)
print(car1)
print(car1.__private)

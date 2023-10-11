class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def walk(self):
        return

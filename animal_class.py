from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speed(self):
        pass


class Lion(Animal):
    def speed(self) -> None:
        print("Tha maximum speed : 80km/h")


class Cheeta(Animal):
    def speed(self) -> None:
        print("The maximum speed : 125km/h")

from abc import ABC, abstractmethod


class mamals(ABC):
    def __init__(self) -> None:
        self.cls = "Mammals"

    @abstractmethod
    def display(self):
        pass


class Person(mamals):
    def __init__(self, name="Default") -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def display(self):
        print(self.name)


class Employee(Person):
    static_variable = 0

    def __init__(self, name, salary, post) -> None:
        self.salary = salary
        self.post = post
        self.static_variable = Employee.static_variable
        super().__init__(name)


emp = Employee("Rahul", 200000, "Intern")
emp.display()
print(emp.static_variable)
print(Employee.static_variable)

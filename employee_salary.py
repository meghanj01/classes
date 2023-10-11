class Employee:
    def __init__(self, employee_id, salary, num_hours):
        self.employee_id = employee_id
        # if salary < 5:
        #     self.salary = salary + 1
        # elif num_hours > 6:
        #     self.salary = salary + 5
        # else:
        #     self.salary = salary
        self.num_hours = num_hours

    def get_salary(self):
        return self.salary

    # @get_salary.setter
    # def add_sal(self):
    #     if self.salary < 5:
    #         self.salary = self.salary + 1

    # @get_salary.setter
    # def add_work(self):
    #     if self.num_hours > 6:
    #         self.salary = self.salary + 6


emp = Employee(1, 8, 8)
print(emp.get_salary())

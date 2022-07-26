class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        # self.id = id + 50
        # self.name = name
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


employee_1 = SalaryEmployee(123, "Harriet Ginger", 700000)

print(employee_1.name)
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self._employee_id = employee_id
        self._name = name
        self._department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._employee_id}")
        print(f"Employee Name: {self._name}")
        print(f"Department: {self._department}")

class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self._basic_salary = basic_salary
        self._bonus = bonus

    def calculate_salary(self):
        return self._basic_salary + self._bonus

    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self._basic_salary:.2f}")
        print(f"Bonus: ${self._bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")
        print()

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self._hourly_rate:.2f}")
        print(f"Hours Worked: {self._hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")
        print()

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self._stipend = stipend

    def calculate_salary(self):
        return self._stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self._stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")
        print()

# Example Usage
permanent_employee = PermanentEmployee("1001", "Ajay", "IT", 60000, 5000)
contract_employee = ContractEmployee("1002", "Kumar", "HR", 50, 160)
intern = Intern("1045", "Rohit", "Finance", 1500)

permanent_employee.display_details()
contract_employee.display_details()
intern.display_details()

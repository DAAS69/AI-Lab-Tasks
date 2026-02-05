class Employee:
  def __init__(self, name, emp_id):
    self.name = name
    self.emp_id = emp_id

  def calculate_salary(self):
    pass

  def display_details(self):
    print(f'Employee name: {self.name}')
    print(f'Employee id: {self.emp_id}')


class FullTimeEmployee(Employee):
  def __init__(self, name, emp_id, monthly_salary):
    super().__init__(name, emp_id)
    self.monthly_salary = monthly_salary

  def calculate_salary(self):
    print(f'salary is: {self.monthly_salary}')


class PartTimeEmployee(Employee):
  def __init__(self, name, emp_id, hourly_rate, hours_worked):
    super().__init__(name, emp_id)
    self.hourly_rate = hourly_rate
    self.hours_worked = hours_worked

  def calculate_salary(self):
    print(f'salary is: {self.hourly_rate * self.hours_worked}')

  
f1 = FullTimeEmployee('Ali', 101, 50000)
p1 = PartTimeEmployee('Ahmed', 102, 1000, 10)

f1.display_details()
f1.calculate_salary()

p1.display_details()
p1.calculate_salary()

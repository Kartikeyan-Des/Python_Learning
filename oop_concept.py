class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_raise(self):
        self.salary += 5000  
        print(f"💰 {self.name} just got a raise! New Salary: ₹{self.salary}")

    def show_details(self):
        print(f"Name: {self.name} | Dept: {self.department} | Salary: ₹{self.salary}")

emp1 = Employee("Arun", 8000, "Developer")

print("Before Raise:")
emp1.show_details()

emp1.give_raise()

print("After Raise:")
emp1.show_details()
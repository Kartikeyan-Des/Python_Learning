# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def give_raise(self):
#         self.salary += 5000  
#         print(f"💰 {self.name} just got a raise! New Salary: ₹{self.salary}")

#     def show_details(self):
#         print(f"Name: {self.name} | Dept: {self.department} | Salary: ₹{self.salary}")

# emp1 = Employee("Arun", 8000, "Developer")

# print("Before Raise:")
# emp1.show_details()

# emp1.give_raise()

# print("After Raise:")
# emp1.show_details()


# class Cat:

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def cat_meows(self):
#         print(f"{self.name} says meow")

# cat1 = Cat("Marla",3)
# cat2 = Cat("carla",4)


# cat1.cat_meows()
# cat2.cat_meows()

# print(cat1.name, cat1.age)



# class books:
#     def __init__(self,title, author):
#         self.title = title
#         self.author = author

#     def describe(self):
#         print(f"{self.title} is Written by {self.author}")

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

# book1 = books("dust & shadows", "Kit Harrington")
# book2 = books("The Blue Moon", "Mellow Brooks")

# book1.describe()
# book2.describe()

# print(book2)



# print(f"Book 1:  {book1.title}, {book1.author}")
# print(f"Book 2:  {book2.title}, {book2.author}")
         


# Inheritance from the class

class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def drive(self):
        print(f"The {self.brand} is driving")

    def __str__(self):
        return f"'{self.brand}'"

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is Driving")

class Bike(Vehicle):
    def drive(self):
        print(f"The {self.brand} is Driving")

    
car1 = Car("KIA")
Bike1 = Bike("Yamaha")

car1.drive()
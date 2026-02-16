a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
choice = input("Enter Operators: ")

def add(a, b):
  return a + b
def sub(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if b == 0:
    return "Error! Cannot divide by zero"
  return a /b

if choice == '+' or choice.lower() == "add":
  print(add(a, b))
elif choice == '-' or choice.lower() == "subtract":
  print(sub(a, b))
elif choice == '*' or choice.lower() == "multiply":
  print(multiply(a, b))
elif choice == '/' or choice.lower() == "Divide":
  print(divide(a, b))
else:
  print("Unidentified Operator")
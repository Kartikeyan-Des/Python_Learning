num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def find_max(num1,num2):
  if num1 > num2:
    return num1
  else:
    return num2
  
biggest = find_max(num1,num2)
print(f"the biggest number is: {biggest}")
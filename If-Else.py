Age = int(input("Enter your Age: "))

if(Age >= 18):
  print("Your Are An Adult")
else:
  print("you are a Minor")

num = int(input("Enter a Number: "))

if num > 0:
  print(num," is a Positive Number")

elif num < 0:
  print(num," is a Negative Number")

elif num == 0:
  print("It is Zero")

else:
  print("Not a Number")


num1 = int(input("Enter Number: "))

if num1 % 2 == 0:
    print(num1,"is an Even Number")
elif num1 %2 != 0:
    print(num1,"is an Odd number")
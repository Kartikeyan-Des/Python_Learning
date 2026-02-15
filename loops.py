# for i in range(1,101):
#     print(i)

# count = 2

# while count <= 100:
#   print(count)
#   count = count + 1
  
# While loop version
# limit = int(input("Enter  a limit: "))
# total = 0 
# count = 1

# while count <= limit:
#   total = total + count
#   count = count + 1
# print(total)


#for loop version
# limit = int(input("Enter  a limit: "))
# total = 0 
# for i in range(1,limit + 1):
#   total = total + i
# print(total)


#Multiplication table

num = int(input("Enter the number for table: "))

for i in range(1,11):
  result = num * i
  print(f"{num} x {i} = {result}")
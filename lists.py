marks = []

for i in range(1,6):
  score = int(input(f"Enter marks for subject {i}: "))
  marks.append(score)

print("Your mark list ",marks)

total = sum(marks)
average = total / 5

print(f"total marks: {total}")
print(f"Average: {average} ")


numbers = [7,9,2,12,10]

highest = numbers[0]

for num in numbers:
  if num > highest:
    highest = num

print(f"Highest in the list is : {highest}")

prices = [100, 500, 20, 1500, 300, 80, 50, 2000]
affordable_items = [] 

budget = int(input("Enter your Budget: "))

for num in prices:

  if num <= budget:
      affordable_items.append(num)

print(f"Items you can afford: {affordable_items}")
print(f"Total count: {len(affordable_items)}")

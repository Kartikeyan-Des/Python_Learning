for i in range(1, 6):
    print("Number:", i)


count = 1

while count <= 5:
    print("Count is", count)
    count += 1


names = ["Arun", "Karthik", "Meena", "Divya"]

for name in names:
    print(name.upper())


numbers = [12, 45, 7, 23, 56, 19, 30]

total = 0
even_numbers = []

for num in numbers:
    total += num
    if num % 2 == 0:
        even_numbers.append(num)

print("Total:", total)
print("Even numbers:", even_numbers)

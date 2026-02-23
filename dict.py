name_input = input("Enter your Name: ")
phone_input = int(input("Enter your Phone No: "))


contact = {"Name": name_input,
           "Phone": phone_input
}
print(contact)

# Task 2

count = int(input("Enter How Many Students: "))

classroom = []

for i in range(count):
  stu_name = input("Enter Student Name: ")
  stu_mark = int(input("Enter Student Mark: "))

  Stu_info = {"Name" : stu_name, "Mark" : stu_mark}

  classroom.append(Stu_info)

print(classroom)
# with open("test.txt", "w") as f:
#   f.write("I'm learning the file handling")


# with open("test.txt", "a") as f:
#   data = input("what did you learn today: ")
#   f.write("\n" + data )

with open("test.txt","r") as f:
  content = f.read()
  print(content)
import calculator_logic

n1 = int(input("Number 1: "))

n2 = int(input("Number 2: "))

n = int(input("Number n: "))

add_result = (calculator_logic.add(n1,n2))

sub_result = (calculator_logic.subtract(n1,n2))

square_rt = (calculator_logic.square(n))

print("Addition Results: ",add_result)
print("Subtraction Results: ",sub_result)
print("square root Results: ",square_rt)
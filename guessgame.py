import random

secret_number = random.randint(1,100)
guess = None
attempts = 0

while guess != secret_number:
  guess = int(input("Enter the number: "))
  attempts += 1
  if(guess > secret_number):
    print("too high,try again but lower")
  elif(guess < secret_number):
    print("too less, try again a bit higher")
  
print(f"you got it in {attempts} attempts!!")

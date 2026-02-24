word = input("Enter Palindrom Word: ").lower()

reversed_word = word[::-1]
if reversed_word == word:
  print(f"{reversed_word} is a Palindrome")
elif reversed_word != word:
  print(f"{reversed_word} is not a palindrome")

sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"

count = 0 

for char in sentence:
  if char in vowels:
    count += 1

print("Number of Vowels: ",count)

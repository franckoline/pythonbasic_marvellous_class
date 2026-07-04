# 1. Reverse a string
print("Question 1 (Reverse a string).")
name = input("Enter your name: ")
name = name[::-1]
print(name)

# 2. Vowel counter
print("\nQuestion 2(Vowel counter).")
vowel = 0
word = input("Enter a word: ")
word = word.casefold()

for i in range(len(word)):
    if word[i] == "a":
        vowel = vowel + 1
    if word[i] == "e":
        vowel = vowel + 1
    if word[i] == "i":
        vowel = vowel + 1
    if word[i] == "o":
        vowel = vowel + 1
    if word[i] == "u":
        vowel = vowel + 1

if vowel == 1:
    print(f"There is {vowel} vowel in {word}")
elif vowel > 1:
    print(f"There are {vowel} vowels in {word}")
elif vowel == 0:
    print(f"There are no vowel in {word}")

# 3. Palindrome checker

print("\nQuestion 3(Palindrome checker).")
word = input("Enter a word: ")

new_word = word[::-1]

if word == new_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

# 4. Whitespace remover
print("\nQuestion 4(Whitespace remover).")
word = input("Enter a word: ")
word = word.replace(" ", "")
print(word)

# 5. Capitalize first letter of each word.
print("\nQuestion 5(Capitalize first letter of each word).")
word = input("Enter a word: ")
word = word.title()
print(word)

# 6. Find and replace
print("\nQuestion 6(Find and replace).")
sentence = input("Enter a sentence that contains the word (bad) :  ")
new_sentence = sentence.replace("bad", "good")
print(new_sentence)

# 7. Character frequency
print("\nQuestion 7(Character frequency).")
word = input("Enter a word: ")

for i in range(len(word)):
    result = word.count(word[i])
    print(f"{word[i]} appeared {result} time(s)")

# 8. Extract domain from email
print("\nQuestion 8(Extract domain from email).")
email = input("Enter an email: ")
domain = email.partition("@")

print(f"The domain of the email is {domain[2]}")

# 9. Check string start and end
print("\nQuestion 9(Check string start and end).")

sentence = input("Enter a sentence: ")
result1 = sentence.startswith("Hello")
result2 = sentence.endswith("World")

if result1:
    print("The sentence starts with Hello,")
else:
    print("The sentence does not start with Hello,")

if result2:
    print("The sentence ends with World.")
else:
    print("The sentence does not end with world.")

# 10. Convert to leetspeak

print("\nQuestion 10(Convert to leetspeak).")
word = input("Enter a word: ")
word = word.replace("A", "4")
word = word.replace("E", "3")
word = word.replace("I", "1")
word = word.replace("O", "0")
word = word.replace("T", "7")

print(word)

# 11. Word count
print("\nQuestion 11(Word count).")
sentence = input("Enter a sentence: ")

result = sentence.split()
print(f"The sentence has {len(result)} word(s)")

# 12. Print every second character
print("\nQuestion 12(Print every second character).")
word = input("Enter a word: ")
second_character = word[1:2]
print(second_character)

# 13.Remove punctuations
print("\nQuestion 13(Remove punctuations).")
sentence = input("Enter a sentence: ")

new_sentence = sentence.replace(".","")
new_sentence = new_sentence.replace(",","")
new_sentence = new_sentence.replace("?","")
new_sentence = new_sentence.replace("!","")
new_sentence = new_sentence.replace("'","")

print(new_sentence)

# 14. Get initials from full name
print("\nQuestion 14(Get initials from full name).")
name = input("Enter your full name: ")
name = name.split()
for i in range(len(name)):
    print(f"Your initial is {name[i][0]}.", end = "")

# 15. Find the longest word


#16. Swapcase
print("\n\nQuestion 16(Swapcase).")
word = input("\nEnter a word: ")
word = word.swapcase()
print(word)

# 17. Check if all characters are digits
print("\nQuestion 17(Check if all characters are digits).")
word = input("Enter anything: ")
word = word.isdigit()

if word:
    print("All characters are digits.")
else:
    print("Not all characters are digits.")

# # 18. Print unique characters
# print("\nQuestion 17(Print unique characters).")
# word = input("Enter a word: ")
#
# for i in range(len(word)):
#     number[i] = word.count(word[i])
#
# print(number)


# 19. Centre align a string
print("\nQuestion 19(Centre align a string).")
word = input("Enter a word: ")
word = word.center(140)
print(word)

# 20. Custom string formatter
print("\nQuestion 20(Custom string formatter).")
name  = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello {name}, you are {age} years old.")


import random
# Hangman1
print("Hangman")
print("The game will be available soon")
# Hangman2
print("HANGMAN")
word = input("Guess the word:\n>")
if word == "python":
    print("You survived!")
else:
    print("You lost!")
# Hangman3
words = ["python", "java", "linux", "php" ]
b = input("Guess the word (python, java, linux, php):>")
if b == random.choice(words):
    print("You survived!")
else:
    print("You lost")




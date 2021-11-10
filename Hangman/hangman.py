import random
# "Hangman 1-st stage"
print("HANGMAN")
print("The game will be available soon")
# "Hangman 2-nd stage"
print("HANGMAN")
word = input("Guess the word:\n>")
if word == "python":
    print("You survived!")
else:
    print("You lost!")
# "Hangman 3-rd stage"
words = ('python', 'java', 'javascript', 'php')
user_input = input("Guess the word:\n>")
run = random.choice(words)
if user_input == words:
    print("You survived!")
else:
    print("You lost!")


















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
# Hangman4
words = ["fire", "earth", "water", "ice"]
r = random.choice(words)
v = "-" * len(r[2:])
guess = input("Guess the word (fire, earth, water, ice) "+(r[:2]+v)+":>")
if guess == r:
    print("You survived!")
else:
    print("You lost!")
# Hangman5
words = ["sword", "axe", "shield", "boom"]
word = random.choice(words)
u = "_" * len(word)
g = False
tries = 8
l = []
print(u)
while not g and tries > 0:
    s = input("Input a letter: >").lower()
    if len(s) == 1:
        if s in word:
            l.append(s)
            word_list = list(u)
            f = [i for i, letter in enumerate(word) if letter == s]
            for index in f:
                word_list[index] = s
            u = "".join(word_list)
            if "_" not in u:
                print("The word is", word, "\nYou win")
                break
            tries -= 1
            print(u)
        else:
            tries -= 1
            print("That letter doesn't appear in the word")
else:
    print("Thank for playing!\nWe'll see how well you did in the next stage")
# Hangman6
words = ["fire", "earth", "water", "ice"]
word = random.choice(words)
u = "_" * len(word)
guessed = False
tries = 8
le = []
print(u)
while not guessed and tries > 0:
    g = input("Input a letter: >").lower()
    if len(g) == 1:
        if g in word:
            if g in le:
                tries -= 1
                print("No improvements")
            le.append(g)
            word_list = list(u)
            indices = [i for i, letter in enumerate(word) if letter == g]
            for index in indices:
                word_list[index] = g
            u = "".join(word_list)
            print(u)
            if "_" not in u:
                guessed = True
                print("The word is", word, "\nYou win")
        else:
            tries -= 1
            print("That letter doesn't appear in the word")
else:
    print("Thanks for playing!\nWe'll see how well you did in the next stage")




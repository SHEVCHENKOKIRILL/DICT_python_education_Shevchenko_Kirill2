import random
# # "Hangman 1-st stage"
# print("HANGMAN")
# print("The game will be available soon")
# # "Hangman 2-nd stage"
# print("HANGMAN")
# word = input("Guess the word:\n>")
# if word == "python":
#     print("You survived!")
# else:
#     print("You lost!")
# # "Hangman 3-rd stage"
# words = ('python', 'java', 'javascript', 'php')
# user_input = input("Guess the word:\n>")
# run = random.choice(words)
# if user_input == words:
#     print("You survived!")
# else:
#     print("You lost!")
# # "Hangman 4-th stage"
# words = ('python', 'java', 'javascript', 'linux')
# run_word = random.choice(words)
# k = "_" * len(run_word)
# guessed = False
# tries = 1
# word_letters = []
# print(k)
# while not guessed and tries > 0:
#     guess = input("Input a letter:").lower()
#     if len(guess) == 1:
#         if guess in run_word:
#             word_letters.appened(guess)
#             word_list = list(k)
#             indices = [i for i, letter in enumerate(run_word)if letter == guess]
#             for index in indices:
#                 word_list[index] = guess
#             k = "".join(word_list)
#             if "_" not in k:
#                 print("The word is", run_word, "\nYou survived!")
#                 break
#             tries -= 1
#             print(k)
#         else:
#             tries -= 1
#             print("You lost!")
# "Hangman 5-th stage"
words = ('python', 'java', 'javascript', 'linux')
word = random.choice(words)
under = "_" * len(word)
guessed = False
tries = 1
guessed_letters = []
print(under)
while not guessed and tries > 0:
    guess = input("Input a letter: >").lower()
    if guess in word:
        if guess in guessed_letters:
            tries -= 1
            print("No improvements")
            guessed_letters.appened(guess)
            word_list = list(under)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_list[index] = guess
                under = "".join(word_list)
                print(under)
                if "_" not in under:
                    guessed = True
                    print("The word is", word, "\nYou win")
                else:
                    tries -= 1
                    print("You lost")
























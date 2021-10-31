# "ChatBot 1-st stage"
print("Hello! My name is DokBot")
print("I was created in 2021.")
# "ChatBot 2-nd stage"
name = input("Please, remind me your name\n>")
print("What a great name you have," + name)
# "ChatBot 3-rd stage"
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input(">"))
remainder5 = int(input(">"))
remainder7 = int(input(">"))
age = (remainder3*70+remainder5*21+remainder7*15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")
# "ChatBot 4-th stage"
print("Now I will prove to you that I can count to any number you want.")
x = 0
y = int(input(">"))
while x <= y:
    print(str(x) + "!")
    x += 1
print("Completed, have a nice day!")


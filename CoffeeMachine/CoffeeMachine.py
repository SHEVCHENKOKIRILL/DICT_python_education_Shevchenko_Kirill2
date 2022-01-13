# CoffeeMachine
class CoffeeMachine:
    def __init__(self):
        self.water = 200
        self.milk = 50
        self.beans = 15
        self.cups = 10
        self.money = 50

    def fill(self):
        self.water += int(input("Write how many water do want: > "))
        self.milk += int(input("Write how many milk do want: > "))
        self.beans += int(input("Write how many beans do want: > "))
        self.cups += int(input("Write how many cups do want: > "))

    def esp(self):
        if self.water < 100:
            print("Sorry, enough water in coffee machine.")
        elif self.beans < 20:
            print("Sorry, enough beans in coffee machine.")
        elif self.cups < 1:
            print("Sorry, enough cups in coffee machine.")
        else:
            self.water -= 300
            self.beans -= 20
            self.cups -= 1
            self.money += 10
            print("""Starting make a coffee
            Grinding coffee beans
            Boiling water
            Mixing boiled water with crushed coffee beans
            Pouring coffee into the cup
            Pouring some milk into the cup
            Coffee is ready!""")

    def lat(self):
        if self.water < 300:
            print("Sorry, enough water in coffee machine.")
        elif self.milk < 75:
            print("Sorry, enough milk in coffee machine.")
        elif self.beans < 20:
            print("Sorry, enough beans in coffee machine.")
        elif self.cups < 1:
            print("Sorry, enough cups in coffee machine.")
        else:
            self.water -= 300
            self.milk -= 100
            self.beans -= 10
            self.cups -= 1
            self.money += 7
            print("""Starting make a coffee
            Griding coffee beans
            Boiling water
            Mixing water with crushed beans
            Pouring coffee into cup
            Adding milk into your coffee
            Coffee ready!""")

    def cap(self):
        if self.water < 200:
            print("Sorry, enough water in coffee machine.")
        elif self.milk < 100:
            print("Sorry, enough milk in coffee machine.")
        elif self.beans < 12:
            print("Sorry, enough beans in coffee machine.")
        elif self.cups < 1:
            print("Sorry, enough cups in coffee machine.")
        else:
            self.water -= 250
            self.milk -= 100
            self.beans -= 10
            self.cups -= 1
            self.money += 6
            print("""Starting make a coffee
            Griding coffee beans
            Boiling water
            Mixing water with crushed beans
            Pouring coffee into cup
            Adding milk into your coffee
            Coffee ready!""")

    def take(self):
        print(f"I gave you {self.money} grn.")
        self.money = self.money - self.money

    def remaining(self):
        print(f"""In coffee machine:
        {self.water} of water.
        {self.milk} of milk.
        {self.beans} of beans.
        {self.cups} of cups.
        {self.money} of money.""")


objects = CoffeeMachine()
while True:
    a = str(input("Write action (buy, fill, take, remaining, exit): > "))
    if a == "buy":
        while a != "back":
            selecting = input("What you want buy; 1 - espresso, 2 - latte, 3- cappuccino.")
            if selecting == "1":
                objects.esp()
                break
            if selecting == "2":
                objects.lat()
                break
            if selecting == "3":
                objects.cap()
                break
    if a == "fill":
        objects.fill()
    if a == "take":
        objects.take()
    if a == "exit":
        break
    if a == "remaining":
        objects.remaining()








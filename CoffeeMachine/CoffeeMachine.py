# CoffeeMachine
class CoffeeMachine:
    def __init__(self, water=300, milk=450, coffee=150, cups=10, money=500):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def remaining(self):
        print("The coffee machine has:\n", self.water, "of water\n", self.milk, "of milk\n", self.coffee,
              "of coffee beans\n", self.cups, "of disposable cups\n", self.money, "of money")

    @staticmethod
    def ingredients():
        return input("Write action (buy, fill, take, remaining, exit):\n>")


    def buys(self):
        a = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n>"))
        if a == "1":
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
            self.money += 4
            if self.water < 0:
                print("Sorry, not enough water!")
            elif self.coffee < 0:
                print("Sorry, not enough coffee!")
            elif self.cups < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
        elif a == "2":
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7
            if self.water < 0:
                print("Sorry, not enough water!")
            elif self.coffee < 0:
                print("Sorry, not enough coffee!")
            elif self.cups < 0:
                print("Sorry, not enough cups!")
            elif self.milk < 0:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
        elif a == "3":
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6
            if self.water < 0:
                print("Sorry, not enough water!")
            elif self.coffee < 0:
                print("Sorry, not enough coffee!")
            elif self.cups < 0:
                print("Sorry, not enough cups!")
            elif self.milk < 0:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
        elif a == "back":
            self.ingredients()
        else:
            return self.buys()

    def fills(self):
        b = int(input("Write how many ml of water you want to add:\n>"))
        self.water += b
        c = int(input("Write how many ml of milk you want to add:\n>"))
        self.milk += c
        d = int(input("Write how many grams of coffee beans you want to add:\n>"))
        self.coffee += d
        e = int(input("Write how many disposable coffee cups you want to add:\n>"))
        self.cups += e

    def takes(self):
        print("I gave you", self.money, )
        self.money -= self.money

    def main(self):
        ing = self.ingredients()
        if ing == "buy":
            self.buys()
            self.main()
        elif ing == "fill":
            self.fills()
            self.main()
        elif ing == "take":
            self.takes()
            self.main()
        elif ing == "remaining":
            self.remaining()
            self.main()
        elif ing == "exit":
            exit()
        else:
            return self.main()





























    




                                                        






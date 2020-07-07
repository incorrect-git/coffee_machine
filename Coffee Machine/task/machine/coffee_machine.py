# Write your code here
# number_cups = int(input("Write how many cups of coffee you will need: "))
#
# water = number_cups * 200
# milk = number_cups * 50
# coffee = number_cups * 15
#
# print("For " + str(number_cups) + " cups of coffee you will need:")
# print(str(water) + " of water")
# print(str(milk) + " of milk")
# print(str(coffee) + " of coffee beans")

# water = 200
# milk = 50
# coffee = 15
#
# amount_water = int(input("Write how many ml of water the coffee machine has:"))
# amount_milk = int(input("Write how many ml of milk the coffee machine has:"))
# amount_coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
# cups = int(input("Write how many cups of coffee you will need:"))
#
#
# max_cups_water = amount_water // water
# max_cups_milk = amount_milk // milk
# max_cups_coffee = amount_coffee // coffee
#
# max_cups = min(max_cups_water, max_cups_milk, max_cups_coffee)
#
# if max_cups > cups:
#     print("Yes, I can make that amount of coffee (and even " + str(max_cups - cups) + " more than that)")
# elif max_cups < cups:
#     print("No, I can make only " + str(max_cups) + " cups of coffee")
# else:
#     print("Yes, I can make that amount of coffee")


# water = 200
# milk = 50
# coffee = 15
# disposable_cups = 1
#
# amount_water = int(input("Write how many ml of water the coffee machine has:"))
# amount_milk = int(input("Write how many ml of milk the coffee machine has:"))
# amount_coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
# cups = int(input("Write how many cups of coffee you will need:"))
#
#
# max_cups_water = amount_water // water
# max_cups_milk = amount_milk // milk
# max_cups_coffee = amount_coffee // coffee

# amount_water = 400
# amount_milk = 540
# amount_coffee = 120
# amount_disposable_cups = 9
# amount_money = 550
#
# action = ''
#
#
# # need_for_espresso = { "250", "16", "4" }
# def amount_resources():
#     print("The coffee machine has:")
#     print(amount_water, " of water")
#     print(amount_milk, " of milk")
#     print(amount_coffee, " of coffee beans")
#     print(amount_disposable_cups, " of disposable cups")
#     print(amount_money, " of money")
#
#
# def buy():
#     global amount_milk
#     global amount_water
#     global amount_coffee
#     global amount_disposable_cups
#     global amount_money
#     type_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n > ")
#     if type_buy == "1":
#         if amount_water >= 250 and amount_coffee >= 16:
#             amount_water -= 250
#             amount_coffee -= 16
#             amount_disposable_cups -= 1
#             amount_money += 4
#             print("I have enough resources, making you a coffee!")
#         else:
#             print("Sorry, not enough water!")
#     elif type_buy == "2":
#         if amount_water >= 350 and amount_coffee >= 20 and amount_milk >= 75:
#             amount_water -= 350
#             amount_coffee -= 20
#             amount_milk -= 75
#             amount_disposable_cups -= 1
#             amount_money += 7
#             print("I have enough resources, making you a coffee!")
#         else:
#             print("Sorry, not enough water!")
#     elif type_buy == "3":
#         if amount_water >= 200 and amount_coffee >= 12 and amount_milk >= 100:
#             amount_water -= 200
#             amount_coffee -= 12
#             amount_milk -= 100
#             amount_disposable_cups -= 1
#             amount_money += 6
#             print("I have enough resources, making you a coffee!")
#         else:
#             print("Sorry, not enough water!")
#
#
# def fill():
#     global amount_milk
#     global amount_water
#     global amount_coffee
#     global amount_disposable_cups
#     add_water = int(input("Write how many ml of water do you want to add:\n> "))
#     add_milk = int(input("Write how many ml of milk do you want to add:\n> "))
#     add_coffee = int(input("Write how many grams of coffee beans do you want to add:\n> "))
#     add_cup = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
#     amount_milk += add_milk
#     amount_water += add_water
#     amount_coffee += add_coffee
#     amount_disposable_cups += add_cup
#
#
# def take():
#     global amount_money
#     print("I gave you $", amount_money)
#     amount_money = 0
# amount_resources()
# class CoffeeMachine:
#     amount_water = 400
#     amount_milk = 540
#     amount_coffee = 120
#     amount_disposable_cups = 9
#     amount_money = 550
#     action = ''
#
#     def __init__(self):
#         pass
#
#     def buy(self):
#         type_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n > ")
#         if type_buy == "1":
#             if self.amount_water >= 250 and self.amount_coffee >= 16:
#                 self.amount_water -= 250
#                 self.amount_coffee -= 16
#                 self.amount_disposable_cups -= 1
#                 self.amount_money += 4
#                 print("I have enough resources, making you a coffee!")
#             else:
#                 print("Sorry, not enough water!")
#         elif type_buy == "2":
#             if self.amount_water >= 350 and self.amount_coffee >= 20 and self.amount_milk >= 75:
#                 self.amount_water -= 350
#                 self.amount_coffee -= 20
#                 self.amount_milk -= 75
#                 self.amount_disposable_cups -= 1
#                 self.amount_money += 7
#                 print("I have enough resources, making you a coffee!")
#             else:
#                 print("Sorry, not enough water!")
#         elif type_buy == "3":
#             if self.amount_water >= 200 and self.amount_coffee >= 12 and self.amount_milk >= 100:
#                 self.amount_water -= 200
#                 self.amount_coffee -= 12
#                 self.amount_milk -= 100
#                 self.amount_disposable_cups -= 1
#                 self.amount_money += 6
#                 print("I have enough resources, making you a coffee!")
#             else:
#                 print("Sorry, not enough water!")
#
#     def fill(self):
#         add_water = int(input("Write how many ml of water do you want to add:\n> "))
#         add_milk = int(input("Write how many ml of milk do you want to add:\n> "))
#         add_coffee = int(input("Write how many grams of coffee beans do you want to add:\n> "))
#         add_cup = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
#         self.amount_milk += add_milk
#         self.amount_water += add_water
#         self.amount_coffee += add_coffee
#         self.amount_disposable_cups += add_cup
#
#     def take(self):
#         print("I gave you $", self.amount_money)
#         self.amount_money = 0
#
#     def remaining(self):
#         print("The coffee machine has:")
#         print(self.amount_water, " of water")
#         print(self.amount_milk, " of milk")
#         print(self.amount_coffee, " of coffee beans")
#         print(self.amount_disposable_cups, " of disposable cups")
#         print(self.amount_money, " of money")
#
#
# coffee_machine = CoffeeMachine()
# while True:
#     action = input("Write action (buy, fill, take, remaining, exit) \n> ")
#     if action == 'exit':
#         break
#     elif action == "buy":
#         coffee_machine.buy()
#     elif action == "fill":
#         coffee_machine.fill()
#     elif action == "take":
#         coffee_machine.take()
#     elif action == 'remaining':
#         coffee_machine.remaining()
#     elif action == 'back':
#         continue


class CoffeeMachine:
    state = None
    amount_water = 0
    amount_milk = 0
    amount_coffee = 0
    amount_disposable_cups = 0
    amount_money = 0

    def __init__(self, new_amount_water, new_amount_milk, new_amount_coffee, new_amount_disposable_cups, new_amount_money):
        self.amount_water = new_amount_water
        self.amount_milk = new_amount_milk
        self.amount_coffee = new_amount_coffee
        self.amount_disposable_cups = new_amount_disposable_cups
        self.amount_money = new_amount_money

    # def route(self, new_state):
    def buy(self):
        pass


class Buy:
    def run(self):
        pass


class Fill:
    def run(self):
        add_water = int(input("Write how many ml of water do you want to add:\n> "))
        add_milk = int(input("Write how many ml of milk do you want to add:\n> "))
        add_coffee = int(input("Write how many grams of coffee beans do you want to add:\n> "))
        add_cup = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
        self.amount_milk += add_milk
        self.amount_water += add_water
        self.amount_coffee += add_coffee
        self.amount_disposable_cups += add_cup
        self.state = None


class Remaining:
    def run(self):
        print("The coffee machine has:")
        print(self.amount_water, " of water")
        print(self.amount_milk, " of milk")
        print(self.amount_coffee, " of coffee beans")
        print(self.amount_disposable_cups, " of disposable cups")
        print(self.amount_money, " of money")
        self.state = None


class Take:
    def run(self):
        print("I gave you $", self.amount_money)
        self.amount_money = 0
        self.state = None


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    if coffee_machine.state is None:
        action = input("Write action (buy, fill, take, remaining, exit) \n> ")

    if action == 'exit':
        break
    elif action == 'back':
        coffee_machine.state = None
        continue
    elif action == 'buy':
        Buy.run(coffee_machine)
        continue
    elif action == 'fill':
        Fill.run(coffee_machine)
        continue
    elif action == 'take':
        Take.run(coffee_machine)
        continue
    elif action == 'remaining':
        Remaining.run(coffee_machine)
        continue

    coffee_machine.state = action

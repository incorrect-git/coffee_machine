money = int(input())

if money < 23:
    print("None")
elif 23 <= money < 678:
    budget = (money // 23)
    print(str(budget), "chicken" if budget == 1 else "chickens")
elif 678 <= money < 1296:
    budget = (money // 678)
    print(str(budget), "goat" if budget == 1 else "goats")
elif 1296 <= money < 3848:
    budget = (money // 1296)
    print(str(budget), "pig" if budget == 1 else "pigs")
elif 3848 <= money < 6769:
    budget = (money // 3848)
    print(str(budget), "cow" if budget == 1 else "cows")
elif money >= 6769:
    budget = (money // 6769)
    print(str(budget), "sheep" if budget == 1 else "sheep")

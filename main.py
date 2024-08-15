
name = input("Welcome to the GC Fruit Market! What is your name? ")

fruits = {
    "apple": 2,
    "grape": 1,
    "orange": 3
}

print(f"Welcome {name}. Which fruit would you like to buy?")

totalApples = 0
totalGrapes = 0
totalOranges = 0

while True:
    print("\n1. Apple $2\n2. Grape $1\n3. Orange $3")
    userChoice = input("> ")

    if userChoice == "1":
        totalApples += 1
        print(f"You bought 1 apple at $2")
    elif userChoice == "2":
        totalGrapes += 1
        print(f"You bought 1 grape at $1")
    elif userChoice == "3":
        totalOranges += 1
        print(f"You bought 1 orange at $3")
    else:
        print("Invalid choice, please select a valid fruit.")

    another = input("Would you like to buy another piece of fruit? y/n\n").lower()
    if another != "y":
        break

subtotal = (totalApples * fruits["apple"]) + (totalGrapes * fruits["grape"]) + (totalOranges * fruits["orange"])
tax = subtotal * 0.05
total = subtotal + tax

print(f"Order for {name}")
print(f"{totalApples} apple(s) at $2 apiece")
print(f"{totalGrapes} grape(s) at $1 apiece")
print(f"{totalOranges} orange(s) at $3 apiece")
print(f"Sub Total: ${subtotal}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total}")
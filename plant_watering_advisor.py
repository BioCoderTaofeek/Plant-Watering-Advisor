plant = input("Enter plant name: ")
days = int(input("How many days since last watering? "))

if days >= 7:
    print("URGENT! " + plant + " is drying 😭")
elif days >= 3:
    print(plant + " needs water 💧")
else:
    print(plant + " is still okay 🌿")  # <- closing parenthesis added
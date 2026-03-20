plants = {}

num_plants = int(input("How many plants do you want to track? "))
print(f"Tracking {num_plants} plants...")  # 
for i in range(num_plants):
    name = input("Enter plant name: ")
    days = int(input("How many days since last watering? "))
    plants[name] = days

print("\n--- Plant Status ---")

for plant, days in plants.items():
    if days >= 7:
        print("URGENT! " + plant + " is drying 😭")
    elif days >= 3:
        print(plant + " needs water 💧")
    else:
        print(plant + " is still okay 🌿")
total = 0
meal = input(
    "Welcome to Atlas Restaurant!\n"
    "\n"
    "Choose a meal: \n"
    "1. Burger $10 \n"
    "2. Pizza $15 \n"
    "3. Pasta $12 \n"
    ).strip().lower()

if meal == "burger" :
    total += 10
    meal_status = "✔ Burger"
elif meal == "pizza" :
    total += 15
    meal_status = "✔ Pizza"

elif meal == "pasta":
    total += 12
    meal_status = "✔ Pasta"


else:
        print("\nSorry, We don't serve that dish today")
        meal_status = "✖ meal"

if meal_status != "✖ meal":
    drink = input("Add a Drink ($3)? (Y/N): ").strip().lower()
    if drink == "y":
        drink_status = "✔ Drink"
        total += 3
    else:
        drink_status = "✖ Drink"

    dessert = input("Add Dessert ($4)? (Y/N): ").strip().lower()
    if dessert == "y":
        dessert_status = "✔ Dessert"
        total += 4
    else: 
        dessert_status = "✖ Dessert"
    print("\nYou Ordered\n"
    f"{meal_status} \n"
    f"{drink_status} \n"
    f"{dessert_status} \n"
    f"Your total is ${total}" )
else: 
    print("Visit us again soon!")
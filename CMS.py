# Define the menu of the restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Greet
print("Welcome to PYTHON Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
order_items = []

while True:
    item = input("Enter the name of item you want to order: ")
    if item.capitalize() in menu:
        order_total += menu[item.capitalize()]
        order_items.append(item.capitalize())
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Ordered item {item} is not available yet!")

    another_order = input("Do you want to add another item? (Yes/No) ")
    if another_order.lower() != "yes":
        break

print(f"Your ordered items: {', '.join(order_items)}")
print(f"The total amount to pay is: Rs{order_total}")

"""
Dictionary game
Given a menu food
Then Select a food item
Calculate the total
print it out
"""
menu = {"pizza": 3.00,
        "popcorn": 5.5,
        "fries": 6.7,
        "chips": 10.0,
        "lemonade": 40.9,
        "coke": 5.7}
cart = []  # define the cart as list var
total = 0

# print menu first
print("------ menu ------".upper())
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------END--------")

# select food, if not select q to quit
is_quit = False
food_menu_items = menu.keys()
while not is_quit:
    input_food_item = input("Please select food item (select q to quit): ").lower()
    if input_food_item in food_menu_items:
        cart.append(input_food_item)
    elif input_food_item == "q":
        is_quit = True

print()
print("----YOUR ORDER-----")
for cart_item in cart:
    print(f"{cart_item:10}: ${menu.get(cart_item)}")
    total += menu.get(cart_item)
print(f"The total of your order is ${total:.2f}")

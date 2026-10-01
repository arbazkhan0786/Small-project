import hashlib

users = {}

def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    users[username] = hashlib.sha256(password.encode()).hexdigest()
    print("User registered successfully.")

def login():
    username = input("Enter username: ")
    if username not in users:
        print("Username not found.")
        return False
    password = input("Enter password: ")
    if users[username] == hashlib.sha256(password.encode()).hexdigest():
        print("Login successful.")
        return True
    else:
        print("Incorrect password.")
        return False

# Sample usage
print("1. Register\n2. Login")
choice = input("Enter choice: ")
if choice == '1':
    register()
elif choice == '2':
    login()
else:
    print("Invalid choice.")

#Restaurant and Menu Management
restaurants = {}

def add_restaurant():
    name = input("Enter restaurant name : ")
    if name in restaurants:
        print("Restaurant already exists.")
        return
    restaurants[name] = {}
    print("Restaurant added successfully.")

def add_menu_item():
    restaurant = input("Enter restaurant name: ")
    if restaurant not in restaurants:
        print("Restaurant not found.")
        return
    item = input("Enter menu item name: ")
    price = float(input("Enter price: "))
    restaurants[restaurant][item] = price
    print("Menu item added successfully.")

def view_menu():
    restaurant = input("Enter restaurant name: ")
    if restaurant not in restaurants:
        print("Restaurant not found.")
        return
    print(f"Menu for {restaurant}:")
    for item, price in restaurants[restaurant].items():
        print(f"{item}: ${price:.2f}")

# Sample usage
print("1. Add Restaurant\n2. Add Menu Item\n3. View Menu")
choice = input("Enter choice: ")
if choice == '1':
    add_restaurant()
elif choice == '2':
    add_menu_item()
elif choice == '3':
    view_menu()
else:
    print("Invalid choice.")

#Order Processing
orders = []

def place_order():
    restaurant = input("Enter restaurant name: ")
    if restaurant not in restaurants:
        print("Restaurant not found.")
        return
    print(f"Menu for {restaurant}:")
    for item, price in restaurants[restaurant].items():
        print(f"{item}: ${price:.2f}")
    
    order = {}
    while True:
        item = input("Enter item to order (or 'done' to finish): ")
        if item == 'done':
            break
        if item not in restaurants[restaurant]:
            print("Item not found.")
            continue
        quantity = int(input("Enter quantity: "))
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity
    
    total = sum(restaurants[restaurant][item] * quantity for item, quantity in order.items())
    orders.append((restaurant, order, total))
    print(f"Order placed successfully. Total: ${total:.2f}")

def view_orders():
    for i, (restaurant, order, total) in enumerate(orders, 1):
        print(f"Order {i}:")
        print(f"Restaurant: {restaurant}")
        for item, quantity in order.items():
            print(f"{item} x{quantity}")
        print(f"Total: ${total:.2f}")

# Sample usage
print("1. Place Order\n2. View Orders")
choice = input("Enter choice: ")
if choice == '1':
    place_order()
elif choice == '2':
    view_orders()
else:
    print("Invalid choice.")

#Putting It All Together
def main():
    while True:
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Add Restaurant")
        print("4. Add Menu Item")
        print("5. View Menu")
        print("6. Place Order")
        print("7. View Orders")
        print("8. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            add_restaurant()
        elif choice == '4':
            add_menu_item()
        elif choice == '5':
            view_menu()
        elif choice == '6':
            place_order()
        elif choice == '7':
            view_orders()
        elif choice == '8':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
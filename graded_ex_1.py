# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    print("Available categories:")
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    while True:
        try:
            choice = int(input("Select a category: ")) - 1
            if 0 <= choice < len(products):
                return choice
            else:
                print("Invalid choice, please select again.")
        except ValueError:
            print("Please enter a valid number.")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    print("Your cart contains:")
    for item in cart:
        product, price, quantity = item
        cost = price * quantity
        print(f"{quantity} x {product} - ${price} = ${cost}")
        total_cost += cost
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:")
    for item in cart:
        product, price, quantity = item
        cost = price * quantity
        print(f"{quantity} x {product} - ${price} = ${cost}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email and email.strip() != ""

def main():
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter your full name (First Last).")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    cart = []
    while True:
        category_index = display_categories()
        category = list(products.keys())[category_index]
        products_list = products[category]
        
        while True:
            display_products(products_list)
            print("Options:")
            print("1. Select a product to buy")
            print("2. Sort the products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")

            action = input("Choose an action: ")

            if action == "1":
                try:
                    product_index = int(input("Select a product number: ")) - 1
                    if 0 <= product_index < len(products_list):
                        quantity = input("Enter quantity: ")
                        if quantity.isdigit() and int(quantity) > 0:
                            add_to_cart(cart, products_list[product_index], int(quantity))
                        else:
                            print("Invalid quantity.")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter a valid number.")
                
            elif action == "2":
                sort_order = input("Sort by price (1 for ascending, 2 for descending): ")
                if sort_order in ["1", "2"]:
                    sorted_products = display_sorted_products(products_list, "asc" if sort_order == "1" else "desc")
                    display_products(sorted_products)
                else:
                    print("Invalid choice.")
                
            elif action == "3":
                break
            
            elif action == "4":
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Enter delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return
            
            else:
                print("Invalid action.")

if __name__ == "__main__":
    main()


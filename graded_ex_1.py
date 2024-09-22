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

def display_categories():
    print("Available Categories:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")

def display_products(products_list):
    print("Available Products:")
    for idx, (name, price) in enumerate(products_list, 1):
        print(f"{idx}. {name} - ${price}")

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))

def add_to_cart(cart, product, quantity):
    cart.append((product[0], quantity, product[1] * quantity))

def display_cart(cart):
    if cart:
        print("Your Cart:")
        for idx, (name, quantity, total_price) in enumerate(cart, 1):
            print(f"{idx}. {name} (Quantity: {quantity}) - Total: ${total_price}")
    else:
        print("Your cart is empty.")

def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product in cart:
        print(f"{product[0]} - Quantity: {product[1]} - Total: ${product[2]}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return '@' in email

def main():
    name = input("Enter your full name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter your full name (First Last) with only alphabets.")
        name = input("Enter your full name: ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address containing '@'.")
        email = input("Enter your email address: ")

    cart = []
    total_cost = 0

    while True:
        display_categories()
        category_choice = int(input("Select a category by number (or 0 to exit): "))
        
        if category_choice == 0:
            break
        
        category_keys = list(products.keys())
        if category_choice < 1 or category_choice > len(category_keys):
            print("Invalid category selection. Please try again.")
            continue
        
        selected_category = category_keys[category_choice - 1]
        display_products(products[selected_category])
        
        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = int(input("Select an option: "))
            
            if option == 1:
                product_choice = int(input("Enter the product number you want to buy: "))
                if product_choice < 1 or product_choice > len(products[selected_category]):
                    print("Invalid product selection. Please try again.")
                    continue
                
                quantity = input("Enter the quantity you want to buy: ")
                while not quantity.isdigit() or int(quantity) <= 0:
                    print("Please enter a valid quantity.")
                    quantity = input("Enter the quantity you want to buy: ")
                
                product = products[selected_category][product_choice - 1]
                add_to_cart(cart, product, int(quantity))
                total_cost += product[1] * int(quantity)
            
            elif option == 2:
                sort_order = int(input("Sort by price - 1: Ascending, 2: Descending: "))
                sorted_products = display_sorted_products(products[selected_category], sort_order)
                display_products(sorted_products)
            
            elif option == 3:
                break
            
            elif option == 4:
                break
        
        if option == 4:
            break

    if cart:
        display_cart(cart)
        print(f"Total Cost: ${total_cost}")
        address = input("Enter your delivery address: ")
        generate_receipt(name, email, cart, total_cost, address)
    else:
        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()

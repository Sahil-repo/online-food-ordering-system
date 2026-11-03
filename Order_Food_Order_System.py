menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40}

cart = {}

def add_item():
    item = input("Enter Food Name: ").title()

    if item not in menu:
        print("Item not available")
        return
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity")
        return
    if quantity <= 0:
        print("Invalid quantity")
        return

    cart[item] = cart.get(item, 0) + quantity
    subtotal = sum(menu[i] * q for i, q in cart.items())
    print(f"{item} * {quantity} added to cart | Cart subtotal: {subtotal}")

def remove_item():
    item = input("Enter item to remove: ").title()

    if item in cart:
        del cart[item]
        print("Item removed")
    else:
        print("Item not found")

def checkout():
    if not cart:
        print("Cart is empty")
        return

    subtotal = sum(menu[i] * q for i, q in cart.items())

    # for item in cart:
    #     subtotal += menu[item] * cart[item]

    coupon = input("Enter coupon (SAVE10 or NO): ").upper()

    if coupon == "SAVE10":
        discount = subtotal * 10 /100

    elif coupon == "NO":
        discount = 0
    else:
        print("Invalid coupon code. Order cannot be processed.")
        return

    amount = subtotal - discount
    gst = amount * 5 / 100

    if subtotal >= 300:
        delivery = 0
    else:
        delivery = 40

    total = amount + gst + delivery

    print("\n___Final Bill___")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Gst(5%): {gst:.2f}")
    print(f"Delivery: {delivery:.2f}")
    print(f"Total: {total:.2f}")

while True:
    print("1. Show Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Show Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter Choice: ")
    if choice == "1":
        print(menu)
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        print(cart)
    elif choice == "5":
        checkout()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
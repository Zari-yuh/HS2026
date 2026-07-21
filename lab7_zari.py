import random
# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Zari W
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Arizona and Chips
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be negative.")
        else:
            self.price = amount
    def deliver(self):
        print(f"Here's your {self.name} on ice!")

item1 = Drink("Arizona Green Tea", 0.99)
item2 = Drink("Arizona Iced Tea", 0.99)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)

item1.deliver()
item2.deliver()

# Will print Arizona Green Tea, Arizona Iced Tea.

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: The price wont be set
#   Paste the message you see here: "Price cannot be negative"


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class Chips:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be negative.")
        else:
            self.price = amount
    def deliver(self):
        print(f"Here's your bowl of {self.name}!")

item3 = Chips("Rold Gold Pretzels", 4.99)
item4 = Chips("Rold Gold Pretzels Sticks", 4.99)

print(item3.name)
print(item4.name)
print(item3.price)
print(item4.price)

item3.deliver()
item4.deliver()

# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: Python only runs the method associated with the object's class! 



# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: Arizona Green Tea



# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
store = {"1": item1, "2": item2, "3": item3, "4": item4}
cart = Cart()

welcome_message = ["Welcome to our store!", "Thank you for shopping with us!", "Hope you're having a great day!"]
print(random.choice(welcome_message))

item1.set_price(0.49)
print("Sale!" + item1.name + " is on sale for $" + str(item1.price))

print("\nMenu")
for number, item in store.items():
    print(number + ". " + item.name + " - $" + str(item.price))

while True:
    pick = input("What would you like to add to your cart? (1-4) Or type 'done' to checkout. ")
    if pick == "done":
        break
    elif pick in store:
        cart.add(store[pick])
        print(f"Added {store[pick].name} to your cart.")
    else:
        print("So sorry, that's not on our menu! What else would you like?")

print("\nReceipt")
for item in cart.items:
    print(item.name + " - $" + str(item.price))

print("You bought " + str(len(cart.items)) + " item(s).")

total = 0
for item in cart.items:
    item.deliver()
    total += item.price
print(f"Total: ${total:.2f}")

# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.



# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______________



# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================

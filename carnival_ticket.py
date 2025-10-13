# rory brown - pvcc csc 221
# purpose: compute total price for carnival tickets with optional random discount

import random

# prices
senior_price = 5.50
adult_price = 11.00
child_price = 7.00
toddler_price = 1.50

print("*****welcome to the carnival ticketmaster!*****")

# ask about adults and seniors
adults = int(input("how many adult tickets do you want to purchase? (18+) >> "))
seniors = int(input("how many of the adults are older than 60? >> "))

# clamp in case someone types more seniors than adults
if seniors > adults:
    seniors = adults

# ask about kids and toddlers
children = int(input("how many children tickets do you want to purchase? (17 and under) >> "))
toddlers = int(input("how many of the children are toddlers (under 5)? >> "))

# clamp in case someone types more toddlers than children
if toddlers > children:
    toddlers = children

# split counts so no one is double counted
regular_adults = adults - seniors
regular_children = children - toddlers

# totals by group
adult_total = regular_adults * adult_price + seniors * senior_price
child_total = regular_children * child_price + toddlers * toddler_price

# subtotal
subtotal = adult_total + child_total

# show subtotal exactly like a simple receipt
print(f"total ticket cost: ${subtotal:.2f}")

# random discount if subtotal is more than $45
if subtotal > 45.00:
    percent = random.randint(1, 15)       # 1 through 15 inclusive
    discount_amount = subtotal * (percent / 100.0)
    new_total = subtotal - discount_amount

    print(f"discount applied: {percent}%")
    print(f"new total: ${new_total:.2f}")

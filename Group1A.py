# Author: Noah Hicks, Natali
# This program does what it do.

import random

class Order
    # Create Order Class with burger count attribute.
    # Create random burger method.

class Person
    # Create Person Class 
    # Create customer name attribute
    # Create method for getting a random name from a list.

class Customer
    # Just grabs a name for customer_name attribute
    # Just sets a number 1-20 for burger_count attribute
    # Create Customer Class, super person
    # Create child from order

    # Create a queue of 100 customers
    # Create the customer list
    # Create new customer object with name and burger amount, basically.
    # Add that to the list, does 100 times.

# Create a dictionary to store the burger count for each customer

# Loop through the customer queue and update the dictionary

# Sort the dictionary by the burger count in descending order
list_sorted_customers = sorted(customer_dict.items(), key=lambda x: x[1], reverse=True)

# Print the results
print("Customer Name".ljust(19), "Burgers Ordered")
print("-" * 40)
for customer in list_sorted_customers:
    name = customer[0].ljust(19)
    burgers = str(customer[1])
    print(name, burgers)

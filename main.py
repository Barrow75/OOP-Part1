# Object Orientated
# Creating an Instance = Creating an object

class Item:
    # class attributes - belongs to class itself, can be accessed through instance as well
    pay_rate = 0.8  # pay rate after 20% discount

    # methods - 2 functions inside classes

    # Each instance we create this is called automatically
    # self = passes itself as the first argument when you call the methods.
    #   - Allows us to assign attributes from init methods to prevent us from assigning each instance we create
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


# Instances of the class:
item1 = Item("Phone", 100, 5)
# Assign attributes to the instance of the class:
# item1.name = "Phone" (dont need since init method (self.name))
# item1.price = 100 (all in the item1 instance and the init method)
# item1.quantity = 5

# calling the method:
# item1.calculate_total_price(item1.price, item1.quantity)

item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
# item2.name = "Laptop" (dont need since init method (self.name))
# item2.price = 1000 (all in the item instance and the init method)
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))

# assigning attributes to specific instances individually; Example:
#   item2.has_numpad = False

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# This prints out the __init__ methods
"""
print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
"""
# see all attributes belonging to a specific object and converts them to dictionary
"""
print(Item.__dict__)  # All attributes for class level
print(item1.__dict__)  # All attributes for instance level
"""
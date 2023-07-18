# OOP-Part1
(Object Orientated Programming)
Intro to Classes, Instances, Methods, Attributes 

1) Instances are the same as objects. They are designed to gives functionality
  EXAMPLE:
    # Instances of the class:
   (Use when you have def _ _init_ _(self, name, price, quantity):  
    item1 = Item("Phone", 100, 5)
   # OR
     Assign attributes to the instance of the class:  
     item1.name = "Phone"  
     item1.price = 100   
     item1.quantity = 5  

3) Classes are a blueprint for creating objects
      Includes:
           - 1. Class attributes: Belongs to the class itself and can be accessed through instances as well  
                 Ex: pay_rate = .8  
           - 2. Methods: Functions inside the classes. Provides functionality to the objects  
               Ex:     def __init__(self, name, price, quantity):  
                          self.name = name  
                          self.price = price  
                          self.quantity = quantity  

                      def calculate_total_price(self):  
                          return self.price * self.quantity  

                      def apply_discount(self):  
                          self.price = self.price * self.pay_rate  

   3) Calling a method: Takes a specific function out of the class method and instance and outputs it  
            def apply_discount(self):  
              self.price = self.price * self.pay_rate  

            item1 = Item("Phone", 100, 5)  
            item1.apply_discount()  
            print(item1.price)  
        

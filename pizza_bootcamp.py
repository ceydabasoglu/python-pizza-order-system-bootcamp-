

import csv
from datetime import datetime


with open("Menu.txt", "w") as menu_file:
    menu_file.write("* Please Choose a Pizza Base:\n1: Classic\n2: Margherita\n3: TurkPizza\n4: PlainPizza\n* and sauce of your choice:\n11: Olives\n12: Mushrooms\n13: GoatCheese\n14: Meat\n")


class Pizza:
    def __init__(self,description,cost):
        self.description=description
        self.cost=cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Classic pizza"
        self.cost = 10.0

class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita pizza"
        self.cost = 12.0

class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turk pizza"
        self.cost = 15.0

class PlainPizza(Pizza):
    def __init__(self):
        self.description = "Plain pizza"
        self.cost = 8.0

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Olives(Decorator):
    def __init__(self,component):
        self.component = component
        super().__init__(component)
        self.description="Olive"
        self.cost=2.00

    def get_description(self):
      return f"{self.component.get_description()}, {self.description}"

    def get_cost(self):
      return self.component.get_cost() + self.cost
    
class Mushrooms(Decorator):
    
    def __init__(self, component):
        self.component = component
        super().__init__(component)
        self.description = "Mushrooms"
        self.cost = 2.5
        
    def get_description(self):
        return f"{self.component.get_description()}, {self.description}"

    def get_cost(self):
        return self.component.get_cost() + self.cost
    
class GoatCheese(Decorator):
    def __init__(self, component):
        self.component = component
        super().__init__(component)
        self.description = "Goat cheese"
        self.cost = 3.0
        
    def get_description(self):
        return f"{self.component.get_description()}, {self.description}"
 
    def get_cost(self):
        return self.component.get_cost() + self.cost
      
    
class Meat(Decorator):
    def __init__(self, component):
        self.component = component
        super().__init__(component)
        self.description = "Meat"
        self.cost = 4.0
        
    def get_description(self):
        return f"{self.component.get_description()}, {self.description}"

    def get_cost(self):
        return self.component.get_cost() + self.cost
        

def print_menu():
    print("* Please Choose a Pizza Base:")
    print("1: Classic")
    print("2: Margherita")
    print("3: TurkPizza")
    print("4: PlainPizza")
    print("* and sauce of your choice:")
    print("11: Olives")
    print("12: Mushrooms")
    print("13: GoatCheese")
    print("14: Meat")
    
# The get_sauce_choice() function prompts the user to enter a sauce choice and returns the appropriate Decorator object.
def get_sauce_choice():
    while True:
        try:
            choice = input("Enter your sauce choice (11: Olives, 12: Mushrooms, 13: Goat Cheese, 14: Meat): ")
            if choice not in ['11', '12', '13', '14']:
                print("Invalid sauce choice. Please enter a number between 11 and 14.")
                continue
            return choice
        except ValueError:
            print("Invalid input. Please enter a number between 11 and 14.")


def get_sauce(sauce_choice, pizza):
    if sauce_choice == '11':
        return Olives(pizza)
    elif sauce_choice == '12':
        return Mushrooms(pizza)
    elif sauce_choice == '13':
        return GoatCheese(pizza)
    elif sauce_choice == '14':
        return Meat(pizza)

#The get_pizza_choice() function prompts the user to enter a pizza base choice and returns the appropriate Pizza object.
def get_pizza_choice():
    while True:
        try:
            choice = int(input("Enter your pizza choice: "))
            if choice < 1 or choice > 4:
                print("Invalid pizza choice. Please enter a number between 1 and 4.")
                continue
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

#the add_sauce() function adds the chosen sauce to the chosen pizza and returns the resulting object.
def add_sauce(pizza, sauce):
    pizza_with_sauce = sauce(pizza)
    return pizza_with_sauce

def get_pizza():
    pizza_choice = get_pizza_choice()
    pizza_type = input("What type of pizza would you like? ")
    print("Great! We'll get started on your " + pizza_type + " pizza right away.")
    print("...")
    print("Your " + pizza_type + " pizza is ready!")
    pizza = None
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = PlainPizza()
    while True:
        add_sauce_choice = input("Would you like to add sauce? (Y/N): ")
        if add_sauce_choice.upper() == 'Y':
            sauce_choice = get_sauce_choice()
            if sauce_choice == '11':
                pizza = add_sauce(pizza, Olives)
            elif sauce_choice == '12':
                pizza = add_sauce(pizza, Mushrooms)
            elif sauce_choice == '13':
                pizza = add_sauce(pizza, GoatCheese)
            elif sauce_choice == '14':
                pizza = add_sauce(pizza, Meat)
            print("Your " + pizza_type + " pizza with " + pizza.get_description() + " is ready!")
            break
        elif add_sauce_choice.upper() == 'N':
            print("Your " + pizza_type + " pizza is ready!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    return pizza

def main():
    with open("Menu.txt", "r") as file:
        print(file.read())
    
    
    print_menu()
    pizza = get_pizza()
    
    
    print("Your order is complete. Here's what you ordered:")
    print(pizza.get_description() + " - Cost: $" + str(pizza.get_cost()))
    
    total_cost = print("Total cost: ", pizza.get_cost())
    
    name_surname = input("Enter your name and surname: ")
    tc_number = input("Enter TC Number: ")
    card_number = input("Enter Card Number: ")
    

    
    order_time = datetime.now()

    data = [total_cost ,order_time, name_surname, tc_number, card_number]
    
    
    with open('orders.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Total','Order Time', 'Name Surname', 'Tc No', 'Card No'])
        writer.writerow(data)
if __name__ == '__main__':
    main()
       

    
    
    





    


 



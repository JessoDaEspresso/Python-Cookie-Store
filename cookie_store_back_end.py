import csv

selections = ['C', 'c', "Chocolate Chip", "chocolate chip", 'O', "o", "Oatmeal Raisin", "oatmeal raisin", "Sugar", 'S',
              's', "sugar"]


class Cookie:
    type = "Unbaked"
    price = 0.0
    ice_cream_status = False

    # Constructor
    def __init__(self):
        print("Cookie Created")

    # Type Setter
    def type_selector(self, user_type):
        # if the selection is valid
        if user_type in selections:
            self.type = user_type
        # Standardize choices (if user selected c represent as cookie)
        if user_type == "C" or user_type == "c" or user_type == "Chocolate Chip" or user_type == "chocolate chip":
            self.type = "Chocolate Chip"
            self.update_price()
        elif user_type == "O" or user_type == "o" or user_type == "Oatmeal Raisin" or user_type == "oatmeal raisin":
            self.type = "Oatmeal Raisin"
            self.update_price()
        elif user_type == "S" or user_type == "s" or user_type == "Sugar" or user_type == "sugar":
            self.type = "Sugar"
            self.update_price()
        # Display the selection
        print("Type is now: " + self.type)

    def update_price(self):
        if self.type == "Chocolate Chip":
            self.price = 1.50
        elif self.type == "Oatmeal Raisin":
            self.price = 1.25
        elif self.type == "Sugar":
            self.price = 1.00
        else:
            self.price = 0.00

    def add_ice_cream(self, userSelection):
        # Updating Cookie Price based on Ice Cream
        if userSelection == "Yes" or userSelection == "yes" or userSelection == "y" or userSelection == "Y":
            self.ice_cream_status = True
            self.price += 0.50
            print("Your total is: $" + str(self.price))

    def generate_recipt(self):
        csv.writer(open("recipt.csv", "w")).writerow(["Selections", "Price"])
        csv.writer(open("recipt.csv", "a")).writerow([self.type, self.price])
        if self.ice_cream_status:
            csv.writer(open("recipt.csv", "a")).writerow(["Ice Cream", 0.50])

        price_as_str = str(self.price)
        csv.writer(open("recipt.csv", "a")).writerow(["Total"] + [price_as_str])

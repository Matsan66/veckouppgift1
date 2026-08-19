from item import Item

class Inventory:
    """
    Class Inventory represents the clubs available items for rent
    """
    def __init__(self):
        self.items = []

    def set_item(self, name, rent_price, amount):
        """
        Adds an item to the inventory with name, rent price and amount
        """
        self.items.append(Item(name, rent_price, amount))


    def rent(self, item_name):
        """
        Rents item by name by removing one item from the inventory
        """
        for item in self.items:
            if item.name == item_name:
                if item.amount > 0:
                    item.amount = item.amount - 1

    def get_amount_left(self, name):
        """
        Returns amount of available items left in the inventory
        """
        for item in self.items:
            if item.name == name:
                return item.amount

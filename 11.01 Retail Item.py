class RetailItem:
    def __init__(self, Description, UnitOnHand, Price):
        self.Description = Description
        self.UnitOnHand = UnitOnHand
        self.Price = Price
    def InventoryValue(self): 
        return self.UnitonHand * self.Price


file = open("11.01 Inventory.txt","r")
list = []
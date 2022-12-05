class RetailItem:
  def __init__(self, Description, UnitOnHand,Price):
    self.Description = Description
    self.UnitOnHand = UnitOnHand
    self.Price = Price

  def InventoryValue(self): 
        return (self.UnitOnHand * self.Price)



f = open('10.02 Inventory.txt')

list = []

for i in f:
  line = i.replace('\n','')
  data = line.split(', ')
  
  list.append(RetailItem(data[0],int(data[1]),float(data[2])))

print("{:>11} {:>17} {:>17} {:>17}".format("Description","Unit On Hand","Price","Inventory Value"))

for obj in list:
  print("{:>11} {:>17} {:>17} {:>17}".format(obj.Description,obj.UnitOnHand,obj.Price,'%.2f'%obj.InventoryValue()))

f.close()
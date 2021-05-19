class Product():

  def __init__(self,productId,name,price,ItemsInStock,ItemsReserved):
    self.productId= productId
    self.Name = name
    self.Price = price
    self.ItemsInStock = ItemsInStock
    self.ItemsReserved = ItemsReserved

  def setProductID(self, id):
    self.productId=id

  def getProductID(self):
     return self.productId

  def setName(self, name):
    self.Name = name

  def getName(self):
     return self.Name

  def setPrice(self, price):
     self.Price = price

  def getPrice(self):
     return self.Price

  def setItemsInStock(self, ItemsInStock):
     self.ItemsInStock = ItemsInStock

  def getItemsInStock(self):
     return self.ItemsInStock


  def setItemsReserved(self, ItemsReserved):
     self.ItemsReserved = ItemsReserved


  def getItemsReserved(self):
     return self.ItemsReserved
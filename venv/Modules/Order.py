class Order:

    def __init__(self,orderId,date,product,quantity ):
        self.OrderId = orderId
        self.Date = date
        self.Product = product
        self.Quantity= quantity

    def setOrderId(self, id):
        self.OrderId = id
        return self.OrderId

    def getOrderId(self):
        return self.OrderId

    def setDate(self, date):
        self.Date = date
        return self.Date

    def getDate(self):
        return self.Date

    def setProduct(self, product):
        self.Product = product
        return self.Product

    def getProduct(self):
        return self.Product

    def setQuantity(self, quantity):
        self.Quantity = quantity
        return self.Quantity

    def getQuantity(self):
        return self.Quantity

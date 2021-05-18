import sqlite3


class OrderRepository:
    # denne skal snakke med sqllite for order

    def GetALLOrders(self):
        OrderList = []
        conn = sqlite3.connect('ORDERSDB.db')
        cursor = conn.execute("SELECT OrderId, Date, ProductID, Quantity from ORDERS")
        for row in cursor:
            OrderId = row[0]
            Date = row[1]
            ProductID = row[2]
            Quantity = row[3]
            OrderList.append({'orderid': OrderId, 'Date': Date, 'productid': ProductID, 'Quantity': Quantity})

        conn.close()
        return OrderList

    def getOrdesById(self, id):
        conn = sqlite3.connect('ORDERSDB.db')
        cursor = conn.execute("SELECT OrderId,Date,ProductID,Quantity from ORDERS WHERE OrderId =" + str(id))
        for row in cursor:
            print("OrderId = ", row[0])
            print("Date = ", row[1])
            print("ProductID = ", row[2])
            print("Quantity = ", row[3])
            print("\n")
        print("Operation done successfully");
        conn.close()


orr = OrderRepository()

print(orr.GetALLOrders())


# orr.getOrdesById(1)

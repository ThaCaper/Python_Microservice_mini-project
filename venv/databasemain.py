from ProductAPI.DATA import databaseinit

MENU_PROMPT = """ Product database testing

Please choose one the of the following:

1) Add a product
2) Check on 1 product
3) See all products
4) Update product
5) Delete a product
6) Exit

Your selection:"""


def Menu():
    connection = databaseinit.connect
    databaseinit.CREATE_PRODUCT_TABLE(connection)

    while(user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            name = input("Enter a name: ")
            price = input("Enter a price: ")
            itemsInStock = input("How many in stock?: ")
            itemsReserved = input("How many is reserved?: ")
        elif user_input == "2":
            product = databaseinit.GET_PRODUCT_BY_ID(connection, Id)
            print(product)
        elif user_input == "3":
            products = databaseinit.GET_ALL_PRODUCTS(connection)

            for product in products:
                print(product)
        elif user_input == "4":
            updatedProduct = databaseinit.UPDATE_PRODUCT_BY_ID(connection, Id, product)
             name = input("Enter a name: ")
             price = input("Enter a price: ")
             itemsInStock = input("How many in stock?: ")
             itemsReserved = input("How many is reserved?: ")
        elif user_input == "5":
            databaseinit.DELETE_PRODUCT_BY_ID(connection, Id)
        else:
            print("Invalid input, please try again")
menu()
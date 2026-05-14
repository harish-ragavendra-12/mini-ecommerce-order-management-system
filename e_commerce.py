#mini e-commerce order management system

import json

#add order
def add_order():

    order_id = int(input('Enter your order id: '))
    customer_name = input('Enter your name: ')

    products = []

    total_price = 0

    no_of_products = int(input('Number of products: '))

    for i in range(no_of_products):
        product_name = input('Product name: ')
        product_price = int(input('Product price: '))

        product_details = {
            "product": product_name,
            "price": product_price
        }

        products.append(product_details)

        total_price = total_price + product_price

    new_order = {
        "order_id": order_id,
        "customer": customer_name,
        "items": products,
        "total": total_price
    }

    with open("orders.json", "r") as file:
        orders = json.load(file)

    orders.append(new_order)

    with open("orders.json", 'w') as file:
        json.dump(orders, file, indent=4)

    print("Order added successfully")

#view orders
def view_orders():

    with open("orders.json", "r") as file:
        orders = json.load(file)

    for order in orders:
        print('\nOrder ID:',order['order_id'])
        print('Customer name:',order['customer'])

        print('Products:')

        for item in order['items']:

            print("Product:", item["product"])
            print("Price:", item["price"])

        print('Total:',order['total'])

#search orders
def search_orders():

    user_order_id = int(input('Enter order id: '))

    with open("orders.json", "r") as file:
        orders = json.load(file)

    found = False

    for order in orders:
        if order['order_id'] == user_order_id:
            print('\nOrder ID:', order['order_id'])
            print('Customer:', order['customer'])

            print('Products:')

            for item in order['items']:

                print("Product:", item['product'])
                print("Price:", item['price'])

            print("Total:", order['total'])

            found = True
            break

    if found == False:
        print('No orders available')

#total revenue
def total_revenue():

    with open("orders.json", "r") as file:
        orders = json.load(file)

    total_order_value = 0

    for order in orders:
        total_order_value = total_order_value + order['total']
    return total_order_value


while True:

    print("\n1. Add Order")
    print("2. View Orders")
    print("3. Search Orders")
    print("4. Total Revenue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_order()

    elif choice == "2":
        view_orders()

    elif choice == "3":
        search_orders()

    elif choice == "4":
        print("Total Revenue:", total_revenue())

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")

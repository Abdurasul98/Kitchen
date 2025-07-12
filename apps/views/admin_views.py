from apps.views.views import show_products
from core.file_manager import FileManager
from core.utils import get_next_id


def add_products():
    product_id = get_next_id("products")
    product = input("Product name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    data = [product_id,product,price,quantity]

    FileManager("products").append(data)
    print("Added product")


def delete_products():
    product_id = input("Product id: ")
    file = FileManager("products")
    products = file.read()

    new_products = []
    lampochka = False

    for i in products:
        if i[0] != product_id:
            new_products.append(i)
        else:
            lampochka = True

    if lampochka:
        file.writerows(new_products)
        print("Deleted order")
    else:
        print("Not found this order")


def show_orders():
    orders = FileManager("orders").read()

    for order in orders:
        print(f"ID: {order[0]} Name: {order[1]} Product: {order[2]} Quantity: {order[3]} Phone: {order[4]} Created at: {order[5]}")

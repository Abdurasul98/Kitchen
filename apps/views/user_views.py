from datetime import datetime

from core.file_manager import FileManager
from core.utils import get_next_id
from apps.views.views import show_products, calculate


def time_dec(func):
    def wrapper(*args, **kwargs):
        time_now = datetime.now()
        hour = time_now.hour
        if hour < 12:
            print("Zakaz berishingiz mumkin")
            return func(*args, **kwargs)
        else:
            print("Abet vaqti tugadi, zakaz qabul qilinmaydi")
            return None
    return wrapper

@time_dec
def add_orders():
    product_id = get_next_id(filename="orders")
    full_name = input("Enter full name: ")
    show_products()
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    phone = input("Enter phone number: ")

    time_now = datetime.now()
    created_at = time_now.strftime("%H:%M")

    FileManager("orders").append(row=[product_id, full_name, product_name, quantity, phone, created_at])
    print("New order is added")
    calculate()


def show_my_orders():
    orders = FileManager("orders").read()
    phone = input("Enter phone number: ")

    for order in orders:
        if order[4] == phone:
            print(f"Product: {order[2]} Quantity: {order[4]} Created at: {order[5]}")
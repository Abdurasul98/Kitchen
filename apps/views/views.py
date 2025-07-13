from core.file_manager import FileManager


def show_products():
    products = FileManager("products").read()
    for product in products:
        print(f"ID: {product[0]} Product name: {product[1]} Price: {product[2]} Quantity: {product[3]}")


def calculate(product_name, order_qty):
    products = FileManager("products").read()
    updated_products = []

    for product in products:
        if product[1] == product_name:
            current_qty = int(product[3])
            new_qty = current_qty - int(order_qty)
            if new_qty < 0:
                new_qty = 0
            product[3] = str(new_qty)
        updated_products.append(product)

    FileManager("products").writerows(updated_products)
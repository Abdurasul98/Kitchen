from core.file_manager import FileManager


def show_products():
    products = FileManager("products").read()
    for product in products:
        print(f"ID: {product[0]} Product name: {product[1]} Price: {product[2]} Quantity: {product[3]}")


def calculate():
    orders = FileManager("orders").read()
    products = FileManager("products").read()

    for product in products:
        product_name = product[1]
        product_qty = int(product[3])

        for order in orders:
            if order[2] == product_name:
                ordered_qty = int(order[3])
                product_qty -= ordered_qty

        product[3] = str(product_qty)

    FileManager("products").writerows(products)
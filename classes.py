class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity


class Customer:
    def __init__(self, name, email, order_list):
        self.name = name
        self.email = email
        self.order_list = order_list

    def add_order(self, order):
        self.order_list.append(order)


class Order:
    def __init__(self, product_list, total_price):
        self.product_list = product_list
        self.total_price = total_price

    def add_product(self, product):
        self.product_list.append(product)

    def calculate_total(self):
        self.total_price = 0

        for product in self.product_list:
            self.total_price += product.price

        return self.total_price
from classes import Product, Customer, Order

def load_products(filename):
    products = []
    with open("products.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            name, category, price, quantity = line.split(",")
            product = Product(
                name,
                category,
                float(price),
                int(quantity)
            )
            products.append(product)
    return products

def load_customers(filename):
    customers = []
    with open("customers.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            name, email = line.split(",")
            customer = Customer(
                name,
                email,
                []
            )
            customers.append(customer)
    return customers

new_products = load_products("products.txt")
new_customers = load_customers("customers.txt")

order = Order([], 0)

order.add_product(new_products[0])
order.add_product(new_products[1])

order.total_price = order.calculate_total()

new_customers[0].add_order(order)

print("Загальна сума замовлення: ", order.total_price)

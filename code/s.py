class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}, Address: {self.address}"

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Item: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity

    def check_availability(self, item, quantity):
        if item.name in self.items and self.items[item.name] >= quantity:
            return True
        else:
            return False

class Order:
    def __init__(self, customer, items, shipping_address):
        self.customer = customer
        self.items = items
        self.shipping_address = shipping_address

    def calculate_total_cost(self):
        total_cost = sum(item.total_price() for item in self.items)
        return total_cost

    def validate_order(self, inventory):
        for item in self.items:
            if not inventory.check_availability(item, item.quantity):
                return False
        return True

    def send_confirmation_email(self):
        print(f"Sending confirmation email to {self.customer.email}")

    def update_inventory(self, inventory):
        for item in self.items:
            inventory.add_item(item, -item.quantity)


def main():
    customer = Customer("John Doe", "john@example.com", "123 Main St")
    item1 = Item("Laptop", 1000, 1)
    item2 = Item("Mouse", 20, 2)
    items = [item1, item2]
    shipping_address = "456 Elm St"

    inventory = Inventory()
    inventory.add_item(item1, 5)
    inventory.add_item(item2, 10)

    order = Order(customer, items, shipping_address)

    if order.validate_order(inventory):
        total_cost = order.calculate_total_cost()
        print("Order is valid.")
        print(f"Total cost: ${total_cost}")
        order.send_confirmation_email()
        order.update_inventory(inventory)
        print("Inventory updated.")
    else:
        print("Order validation failed. Item(s) not available.")

if __name__ == "__main__":
    main()

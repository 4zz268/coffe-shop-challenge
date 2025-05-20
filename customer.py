class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters long")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None
        max_spent = 0
        top_customer = None
        for cust in customers:
            spent = sum(order.price for order in cust.orders() if order.coffee == coffee)
            if spent > max_spent:
                max_spent = spent
                top_customer = cust
        return top_customer
